import datetime
import whisper


def textToVTT(result, save_format):
    model = whisper.load_model("base.en")
    result = model.transcribe(
        result)

    with open(save_format, "w") as file:
        for indx, segment in enumerate(result['segments']):
            file.write(str(indx + 1) + '\n')
            # timestamp
            file.write(
                str(datetime.timedelta(seconds=segment['start'])) +
                ' --> ' +
                str(datetime.timedelta(seconds=segment['end'])) +
                '\n')
            file.write(segment['text'].strip() + '\n')
        return result['text']
