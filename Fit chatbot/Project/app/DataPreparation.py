from app.Tokenizers import sentence_tokenizer
import json

def prepareDataForAnalysis():
    f = open('./data.txt','r', errors='ignore')
    raw_doc = f.read()
    raw_doc = raw_doc.lower()
    # nltk.download('punkt')
    # nltk.download('wordnet')
    # nltk.download('omw-1.4')

    sentence_tokens = sentence_tokenizer(raw_doc)
    with open('./sentence_tokens.json', 'w') as json_file:
        json.dump(sentence_tokens, json_file)