from rdflib import Graph, Namespace
import logging
from config import KG_FILE, LOG_FILE
from difflib import get_close_matches
from sentence_transformers import SentenceTransformer, util
import numpy as np

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

# Simple synonym map for demo (expand as needed)
SYNONYMS = {
    'reset password': ['forgot password', 'change password'],
    'support': ['help', 'contact'],
    'account settings': ['profile', 'settings']
}

# Load a lightweight sentence transformer for semantic similarity
try:
    sbert_model = SentenceTransformer('all-MiniLM-L6-v2')
except Exception as e:
    sbert_model = None
    logging.error(f"Could not load sentence transformer: {e}")

def expand_query(query):
    """
    Expand query with synonyms for better KG matching.
    """
    expanded = [query]
    for key, syns in SYNONYMS.items():
        if key in query.lower():
            expanded.extend(syns)
    return expanded

def query_kg(question, kg_file=KG_FILE):
    """
    Query the KG for an answer. Uses fuzzy, synonym, and semantic similarity matching.
    """
    try:
        g = Graph()
        g.parse(kg_file, format='turtle')
        EX = Namespace("http://example.org/faq/")
        q = f'''
        SELECT ?text ?answer WHERE {{
            ?q a {EX.Question.n3()} ;
               {EX.text.n3()} ?text ;
               {EX.answer.n3()} ?answer .
        }}
        '''
        results = list(g.query(q))
        all_questions = [str(row['text']) for row in results]
        all_answers = [str(row['answer']) for row in results]
        # 1. Fuzzy and synonym matching
        expanded = expand_query(question)
        for qtext in expanded:
            matches = get_close_matches(qtext, all_questions, n=1, cutoff=0.7)
            if matches:
                for row in results:
                    if str(row['text']) == matches[0]:
                        logging.info(f"KG answer found for: {question} (fuzzy/synonym)")
                        return str(row['answer'])
        # 2. Semantic similarity (if SBERT available)
        if sbert_model is not None and all_questions:
            question_emb = sbert_model.encode([question])[0]
            kg_embs = sbert_model.encode(all_questions)
            sims = util.cos_sim(question_emb, kg_embs)[0].cpu().numpy()
            best_idx = int(np.argmax(sims))
            if sims[best_idx] > 0.6:
                logging.info(f"KG answer found for: {question} (semantic sim {sims[best_idx]:.2f})")
                return all_answers[best_idx]
        logging.info(f"No KG answer found for: {question}")
        return None
    except Exception as e:
        logging.error(f"Error querying KG: {e}")
        return None

if __name__ == '__main__':
    # Demo
    user_q = "How do I reset my password?"
    answer = query_kg(user_q)
    print(f"Q: {user_q}\nA: {answer}") 