# FIT Chatbot 🤖💬  

**FIT Chatbot** is a custom-built conversational AI system implemented **from scratch**, combining **Python**, **Flask API**, and a lightweight frontend (HTML, CSS, JavaScript).  
The project demonstrates the design of a complete chatbot pipeline, including **data preparation, NLP preprocessing, and response generation**, with an interactive web interface.  

---

## **✨ Features**  
- **From-Scratch NLP Pipeline**:  
  - **Tokenization** (custom rules and preprocessing)  
  - **Lemmatization**  
  - **TF-IDF Vectorization**  
  - **Cosine Similarity** for intent detection  
- **Data Preparation Module** for handling and cleaning training data  
- **Flask API** for serving responses  
- **Web Interface** built with HTML, CSS, and JavaScript for user interaction  
- **Scraper** module for collecting additional data dynamically  
- Modular architecture following **clean coding principles**  

---

## **📂 Project Structure**  
- **`ChatBot.py`** → Main chatbot logic and orchestration  
- **`Constants.py`** → Configuration constants  
- **`CosineSimilarity.py`** → Similarity computation for intent matching  
- **`DataPreparation.py`** → Data cleaning and preprocessing pipeline  
- **`Helpers.py`** → Utility functions  
- **`Lemmatization.py`** → Lemmatization and text normalization  
- **`Routes.py`** → Flask API endpoints for chatbot communication  
- **`Scraper.py`** → Data scraping for enriching chatbot responses  
- **`TFIDFVectorizer.py`** → Custom TF-IDF implementation  
- **`Tokenizers.py`** → Tokenization methods  
- **`__init__.py`** → Package initialization  

---

## **🛠️ Technologies & Tools**  
- **Backend**: Python, Flask  
- **NLP**: Custom tokenization, lemmatization, TF-IDF, cosine similarity  
- **Frontend**: HTML, CSS, JavaScript  
- **Architecture**: Modular Python packages with Flask API integration  

---

## **🚀 How to Run**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/azra-smajic/fit-chatbot.git
   cd fit-chatbot
