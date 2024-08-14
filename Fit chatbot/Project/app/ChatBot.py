from app.TFIDFVectorizer import TFIDFVectorizer
from app.Helpers import translate, split_questions,capitalize_sentences
from app.Lemmatization import LemNormalize
from app.CosineSimilarity import cosine_similarity_single_vs_all
from app.Constants import default_response
import json

with open('./sentence_tokens.json', 'r') as json_file:
    sentence_tokens = json.load(json_file)

def responseChat(user_response, language="en"):
    global sentence_tokens
    questions = split_questions(user_response)
    responses = []

    for question in questions:
        translatedQuestion = translate(question, 'en')
        sentence_tokens.append(translatedQuestion)
        chatResponse = ''
        TfidfVect = TFIDFVectorizer(tokenizer=LemNormalize, stop_words='english')
        tfidf = TfidfVect.fit_transform(sentence_tokens)
        vals = cosine_similarity_single_vs_all(tfidf[-1], tfidf)
        idx = vals.argsort()[-2]  
        flat = vals.flatten()
        flat.sort()
        req_tfidf = flat[-2]
        if req_tfidf == 0:
            chatResponse = default_response
            sentence_tokens.remove(translatedQuestion)
        else:
            chatResponse = sentence_tokens[idx]
            sentence_tokens.remove(translatedQuestion)
            chatResponseCapitalized = capitalize_sentences(chatResponse)
            translatedResponse = translate(chatResponseCapitalized, language)
            print(translatedResponse)
        responses.append(translatedResponse)
    
    return responses