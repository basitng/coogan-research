import whisper
import datetime
import assemblyai as aai
aai.settings.api_key = "48c9dd4c9e274c4795ede224dea42b4e"


def textToVTT(url, save_format):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(url)

    with open(save_format, "w") as file:
        file.write(transcript.export_subtitles_vtt())
        return transcript.text
