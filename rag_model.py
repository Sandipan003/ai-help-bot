from transformers import pipeline
import json
import logging
from config import RAG_MODEL, LOG_FILE
from difflib import get_close_matches

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def rag_fallback(question, context_list):
    """
    Use a lightweight RAG model to answer the question from the most relevant context(s).
    If no relevant context is found, generate a friendly or generic response.
    """
    try:
        # Select top 3 most similar answers as context
        matches = get_close_matches(question, context_list, n=3, cutoff=0.3)
        if matches:
            context = " ".join(matches)
            qa = pipeline("question-answering", model=RAG_MODEL)
            result = qa(question=question, context=context)
            logging.info(f"RAG fallback used for: {question}")
            return result['answer']
        else:
            # If no relevant context, handle greetings or random questions
            greetings = ["hello", "hi", "hey", "greetings"]
            if any(greet in question.lower() for greet in greetings):
                return "Hello! How can I assist you with your help or FAQ questions today?"
            # Generic fallback for random/unanswerable questions
            return "I'm here to help with your account, support, and FAQ questions. Please ask something related to our services!"
    except Exception as e:
        logging.error(f"Error in RAG fallback: {e}")
        return "Sorry, I couldn't find an answer."

if __name__ == '__main__':
    # Demo
    with open('scraped_faqs.json', 'r', encoding='utf-8') as f:
        faqs = json.load(f)
    answers = [faq['answer'] for faq in faqs]
    user_q = "How do I reset my password?"
    print(rag_fallback(user_q, answers)) 