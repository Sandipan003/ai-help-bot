from flask import Flask, request, render_template
from chatbot import query_kg
from rag_model import rag_fallback
import json
import os
import logging
from config import LOG_FILE

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

app = Flask(__name__)

# Load FAQ answers for RAG fallback
if os.path.exists('scraped_faqs.json'):
    with open('scraped_faqs.json', 'r', encoding='utf-8') as f:
        faqs = json.load(f)
    faq_answers = [faq['answer'] for faq in faqs]
else:
    faq_answers = []

@app.route('/health')
def health():
    return {"status": "ok"}, 200

@app.route('/', methods=['GET', 'POST'])
def home():
    answer = ""
    error = None
    question = ""
    if request.method == 'POST':
        question = request.form['question']
        try:
            answer = query_kg(question)
            if not answer and faq_answers:
                answer = rag_fallback(question, faq_answers)
            elif not answer:
                answer = "Sorry, I couldn't find an answer."
        except Exception as e:
            error = str(e)
            logging.error(f"Error in answering: {e}")
            answer = "Sorry, an error occurred."
    return render_template('index.html', answer=answer, error=error, question=question)

if __name__ == '__main__':
    app.run(debug=True) 