from rdflib import Graph, URIRef, Literal, Namespace, RDF
import json
import os
import logging
from config import KG_FILE, LOG_FILE

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def build_kg(faqs, output_file=KG_FILE):
    """
    Build a knowledge graph from FAQ data and serialize to Turtle format.
    """
    try:
        g = Graph()
        EX = Namespace("http://example.org/faq/")
        for idx, faq in enumerate(faqs):
            q_node = URIRef(EX[f"q{idx}"])
            g.add((q_node, RDF.type, EX.Question))
            g.add((q_node, EX.text, Literal(faq['question'])))
            g.add((q_node, EX.answer, Literal(faq['answer'])))
        g.serialize(destination=output_file, format='turtle')
        logging.info(f"Knowledge Graph built with {len(faqs)} FAQs and saved to {output_file}.")
        return g
    except Exception as e:
        logging.error(f"Error building KG: {e}")
        return None

if __name__ == '__main__':
    # For demo: load scraped data from JSON
    scraped_json = 'scraped_faqs.json'
    if os.path.exists(scraped_json):
        with open(scraped_json, 'r', encoding='utf-8') as f:
            faqs = json.load(f)
        build_kg(faqs)
        print(f"Knowledge Graph built with {len(faqs)} FAQs.")
    else:
        print(f"{scraped_json} not found. Run the scraper first.") 