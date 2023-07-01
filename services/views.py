import cloudinary.uploader
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from services.serializers import VideoFileSerializer
from utils.create_csv import create_csv_file
from utils.create_file import create_file
from utils.create_vtt import textToVTT
from utils.extract_sentence import get_sentences
from utils.prompter import Prompter
from utils.send_email import send_email
import assemblyai as aai
aai.settings.api_key = "48c9dd4c9e274c4795ede224dea42b4e"


class GetVideo(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'message': "Done"})


class VideoUploadView(APIView):
    def post(self, request, *args, **kwargs):
        video_file = request.FILES.get('video')
        print("🚀 ~ file: views.py:22 ~ video_file:", video_file)
        response = cloudinary.uploader.upload(
            file=video_file,
            resource_type='video',
            folder='videos/'
        )

        video_url = response['secure_url']
        transcript_file = "transcript.vtt"
        transcript = textToVTT(video_url, transcript_file)
        if transcript == "":
            return Response({'message': "Could not create a video transcript"}, status=status.HTTP_404_NOT_FOUND)

        content = get_sentences(transcript)
        prompter = Prompter(transcript)
        prompter.generate_prompts()
        prompts = prompter.get_prompts()

        data = {
            'video_url': video_url,
            'transcript': transcript
        }
        serializer = VideoFileSerializer(data=data)
        serializer.is_valid()  # Call is_valid() before accessing serializer.data

        image_links = []

        csv_path = "activity.csv"
        file_path = "transcript.txt"
        create_csv_file(content, prompts, csv_path)
        create_file(transcript, file_path)
        send_email(csv_path, transcript_file,
                   file_path, "basitng2004@gmail.com")

        response_data = {
            'serializer': serializer.data,
            'prompts': prompts
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
