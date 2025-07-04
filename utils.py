"""
utils.py
Helper functions for the AI Help Bot project.
"""
import logging
from config import LOG_FILE, LOG_LEVEL

# Logging setup utility

def setup_logging():
    logging.basicConfig(filename=LOG_FILE, level=getattr(logging, LOG_LEVEL), format='%(asctime)s %(levelname)s:%(message)s')

# Synonym expansion utility (for future use)
def expand_with_synonyms(query, synonym_map):
    expanded = [query]
    for key, syns in synonym_map.items():
        if key in query.lower():
            expanded.extend(syns)
    return expanded 