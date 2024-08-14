import re
import random
from googletrans import Translator
from app.Constants import greet_inputs, greet_responses
import spacy
nlp = spacy.load('en_core_web_sm')

def split_questions(user_response):
    split_pattern = re.compile(r'[,.?!]\s*')
    questions = split_pattern.split(user_response)
    
    final_questions = []
    for question in questions:
        sub_questions = re.split(r'\s+and\s+', question)
        final_questions.extend([sq.strip() for sq in sub_questions if sq.strip()])

    return final_questions

def translate(text, language):
    translator = Translator()
    translated = translator.translate(text, dest=language)
    return translated.text

def greet(sentence):
    for word in sentence.split():
        if word.lower() in greet_inputs:
            return random.choice(greet_responses)
        
def capitalize_sentences(text):
    sentences = re.split('([.!?] *)', text)
    capitalized_sentences = ''.join([s.capitalize() for s in sentences])
    return capitalized_sentences