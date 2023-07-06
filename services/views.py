import cloudinary.uploader
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from services.serializers import VideoFileSerializer
from utils.create_csv import create_csv_file
from utils.create_file import create_file
from utils.create_vtt import textToVTT
from utils.extract_sentence import get_sentences
from utils.openai import generate_sentences_prompts
from utils.pickle import PickleData
from utils.prompter import NumberedPromptExtractor
from utils.send_email import send_email


class GetVideo(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'message': "Video retrieval successful!"})


class VideoUploadView(APIView):
    def post(self, request, *args, **kwargs):
        video_file = request.FILES.get('video')
        print("🚀 ~ file: views.py:22 ~ video_file:", video_file)

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
        content = PickleData("audio_content").retrieve_data()
        transcript = PickleData("audio_transcript").retrieve_data()
        prompts = PickleData("audio_prompts").retrieve_data()

        # Create CSV and transcript files
        create_csv_file(content, prompts, csv_path)
        create_file(transcript, file_path)

        # Send email with generated files
        send_email(csv_path, transcript_file,
                   file_path, "basitng2004@gmail.com")

        return Response({'message': "Midjourney image generation complete!"})
