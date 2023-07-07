import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("ASSEMBLY_API_KEY")


class Assemblyai:
    def __init__(self, url):
        self.url = url

    def transcribe_audio(self, audio_url):
        print("Transcribing audio... This might take a moment.")

        headers = {
            "authorization": API_TOKEN
        }

        data = {
            "audio_url": audio_url
        }
        response = requests.post(
            "https://api.assemblyai.com/v2/transcript",
            json=data,
            headers=headers,
        )
        print(response)
        response.raise_for_status()

        transcript_id = response.json()["id"]
        polling_endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"

        while True:
            response = requests.get(polling_endpoint, headers=headers)
            response_data = response.json()

            if response_data["status"] == "completed":
                get_subtitle = self.get_subtitle_file(
                    transcript_id, API_TOKEN, "vtt")
                response_data["export_subtitles_vtt"] = get_subtitle
                return response_data
            elif response_data["status"] == "error":
                raise Exception(
                    f"Transcription failed: {response_data['error']}")
            else:
                time.sleep(3)

    def get_subtitle_file(self, transcript_id, api_token, file_format):
        if file_format not in ["srt", "vtt"]:
            raise ValueError(
                "Invalid file format. Valid formats are 'srt' and 'vtt'.")

        url = f"https://api.assemblyai.com/v2/transcript/{transcript_id}/{file_format}"
        headers = {"authorization": api_token}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.text
        else:
            raise RuntimeError(
                f"Failed to retrieve {file_format.upper()} file: {response.status_code} {response.reason}")

    def Transcriber(self):
        if not self.url:
            print("Upload failed. Please try again.")
            return

        transcript = self.transcribe_audio(self.url)
        print("🚀 ~ file: assemblyai.py:49 ~ transcript:", transcript)
        return transcript
