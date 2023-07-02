
from utils.assemblyai import Assemblyai


def textToVTT(url, save_format):
    assembly = Assemblyai(url=url)
    transcript = assembly.Transcriber()
    print("🚀 ~ file: create_vtt.py:8 ~ transcript:", transcript)

    with open(save_format, "w") as file:
        file.write(transcript['export_subtitles_vtt'])
        return transcript['text']
