import nltk
from nltk.tokenize import sent_tokenize


def get_sentences(content):
    sentences = sent_tokenize(content)
    return sentences


# content = '''Is this a sentence now? Yeah it is a sentence'''

# sentences = get_sentences(content)

# for sentence in sentences:
#     print(sentence)
