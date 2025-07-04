import json
from scraper import scrape_faq
from kg_builder import build_kg
import logging
from config import LOG_FILE

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def main():
    """
    Run the full pipeline: scrape FAQ, save as JSON, and build the KG.
    """
    faqs = scrape_faq()
    if not faqs:
        print("No FAQs scraped. Check your config or source.")
        return
    with open('scraped_faqs.json', 'w', encoding='utf-8') as f:
        json.dump(faqs, f, indent=2)
    build_kg(faqs)
    print(f"[SUCCESS] Scraped {len(faqs)} FAQs and built KG. Ready for chatbot use.")

if __name__ == '__main__':
    main() 