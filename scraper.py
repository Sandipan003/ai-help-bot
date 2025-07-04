import requests
from bs4 import BeautifulSoup
import logging
from config import SCRAPE_URL, USE_LOCAL_HTML, FAQ_ITEM_SELECTOR, QUESTION_SELECTOR, ANSWER_SELECTOR, LOG_FILE

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def scrape_faq(url=SCRAPE_URL, use_local=USE_LOCAL_HTML):
    """
    Scrape FAQ items from a local HTML file or a remote URL.
    Returns a list of dicts with 'question' and 'answer'.
    """
    try:
        if use_local:
            with open(url, encoding='utf-8') as f:
                html = f.read()
        else:
            resp = requests.get(url)
            resp.raise_for_status()
            html = resp.text
        soup = BeautifulSoup(html, 'html.parser')
        faqs = []
        for item in soup.select(FAQ_ITEM_SELECTOR):
            question_elem = item.select_one(QUESTION_SELECTOR)
            answer_elem = item.select_one(ANSWER_SELECTOR)
            if question_elem and answer_elem:
                question = question_elem.get_text(strip=True)
                answer = answer_elem.get_text(strip=True)
                faqs.append({'question': question, 'answer': answer})
        logging.info(f"Scraped {len(faqs)} FAQ items from {'local file' if use_local else url}.")
        return faqs
    except Exception as e:
        logging.error(f"Error scraping FAQ: {e}")
        return []

if __name__ == '__main__':
    faqs = scrape_faq()
    print(faqs) 