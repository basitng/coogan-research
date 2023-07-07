import os
from dotenv import load_dotenv
import cloudinary.uploader
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from midjourney import Midjourney, jsonDecrpter

from services.serializers import VideoFileSerializer
from utils.create_csv import create_csv_file
from utils.create_file import create_file
from utils.create_vtt import textToVTT
from utils.extract_sentence import get_sentences
from utils.openai import generate_sentences_prompts
from utils.pickle import PickleData
from utils.prompter import NumberedPromptExtractor
from utils.send_email import send_email

load_dotenv()


class GetVideo(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'message': "Video retrieval successful!"})


class VideoUploadView(APIView):
    def post(self, request, *args, **kwargs):
        video_file = request.FILES.get('video')
        email = request.data.get('email')

        # Upload video file to Cloudinary
        response = cloudinary.uploader.upload(
            file=video_file,
            resource_type='video',
            folder='videos/'
        )

        video_url = response['secure_url']
        transcript_file = "transcript.vtt"

        # Convert video to VTT transcript
        transcript = textToVTT(video_url, transcript_file)
        if transcript == "":
            return Response({'message': "Could not create a video transcript"}, status=status.HTTP_404_NOT_FOUND)

        # Extract sentences from transcript
        content = get_sentences(transcript)

        # Generate prompts from transcript
        prompts = generate_sentences_prompts(transcript)
        prompt_extractor = NumberedPromptExtractor(prompts)
        prompt_extractor.extract_prompts()
        new_prompts = prompt_extractor.get_prompts()

        # Save data to serializer
        data = {
            'video_url': video_url,
            'transcript': transcript
        }
        serializer = VideoFileSerializer(data=data)
        serializer.is_valid()

        # Store data using Pickle
        PickleData("email").store_pickle_data(email)
        PickleData("audio_transcript").store_pickle_data(transcript)
        PickleData("audio_content").store_pickle_data(content)
        PickleData("audio_prompts").store_pickle_data(new_prompts)

        response_data = {
            'serializer': serializer.data,
            'prompts': new_prompts
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class GenerateMidjourneyImage(APIView):
    def post(self, request, *args, **kwargs):
        images_links = []

        csv_path = "activity.csv"
        file_path = "transcript.txt"
        transcript_file = "transcript.vtt"

        # Retrieve data using Pickle
        email = PickleData("email").retrieve_data()
        content = PickleData("audio_content").retrieve_data()
        transcript = PickleData("audio_transcript").retrieve_data()
        prompts = PickleData("audio_prompts").retrieve_data()

        # Generate images from midjourney using prompts generated
        midjourney = Midjourney(api_key=os.getenv(
            "MIDJOURNEY_API_KEY"), callback_uri="")

        for prompt in prompts:
            seed = midjourney.imagine(prompt=prompt)
            result = midjourney.result(seed=seed)

            if result.get('status') == 'completed':
                response = result
                image_url = response.get('imageUrl')
                images_links.append({
                    'imageUrl': image_url,
                    'prompt': prompt,
                    'seed': seed
                })
            else:
                message = result.get('message')
                print(message)

        # Create CSV and transcript files
        create_csv_file(content, prompts, images_links['imageUrl'], csv_path)
        create_file(transcript, file_path)

        # Send email with generated files
        try:
            send_email(csv_path, transcript_file,
                       file_path, email)
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
            return Response({'message': "Failed to send email"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'message': "Midjourney image generation complete!", 'images': images_links})
