import re

def sentence_tokenizer(text):
    sentence_endings = re.compile(r'([.!?])\s+')
    sentences = sentence_endings.split(text)
    sentences_combined = []
    for i in range(0, len(sentences) - 1, 2):
        sentences_combined.append(sentences[i] + sentences[i+1].strip())
    if len(sentences) % 2 == 1:
        sentences_combined.append(sentences[-1].strip())

    return sentences_combined

def word_tokenizer(text):
    text = text.lower()
    text = re.sub(r'[^\w\s\'\-]', '', text)
    tokens = re.split(r'\s+', text)
    tokens = [token for token in tokens if token]
    return tokens