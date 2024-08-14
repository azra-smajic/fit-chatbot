import nltk 
import string
from app.Tokenizers import word_tokenizer

lemmer = nltk.stem.WordNetLemmatizer()
remove_punc_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
def LemNormalize(text):
    return LemTokens(word_tokenizer(text.lower().translate(remove_punc_dict)))