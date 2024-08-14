# app/routes.py

from flask import jsonify, request
from app import app
from app.DataPreparation import prepareDataForAnalysis
from app.ChatBot import responseChat
from app.Scraper import scrape_and_save
from flask_cors import CORS
CORS(app)
@app.route('/scrapeData', methods=['POST'])
def scrapeData():
    try:
        url = request.json.get('url')
        message = scrape_and_save(url)
        return jsonify({"status": message}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/processData', methods=['GET'])
def processData():
    try:
        prepareDataForAnalysis()
        return jsonify({"status": "OK"}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        new_question = request.json.get('question')
        language = request.json.get('language')
        text = responseChat(new_question, language)
        return jsonify({"message": text}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
