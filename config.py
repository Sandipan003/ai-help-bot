"""
Configuration for the AI Help Bot project.
Edit this file to change scraping targets, selectors, and model settings.
"""

# Scraper settings
SCRAPE_URL = 'sample_data/sample_faq.html'  # Change to your web portal URL for production
USE_LOCAL_HTML = True  # Set to False to scrape from a live website

FAQ_ITEM_SELECTOR = '.faq-item'
QUESTION_SELECTOR = '.faq-question'
ANSWER_SELECTOR = '.faq-answer'

# Knowledge Graph settings
KG_FILE = 'kg.ttl'

# RAG model settings
RAG_MODEL = 'distilbert-base-uncased-distilled-squad'

# Logging settings
LOG_FILE = 'helpbot.log'
LOG_LEVEL = 'INFO' 