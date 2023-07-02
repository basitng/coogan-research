import re


def get_sentences(content):
    # Use regex pattern to match sentences
    pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s'
    sentences = re.split(pattern, content)
    return sentences
