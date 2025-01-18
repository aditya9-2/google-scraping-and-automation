import requests
import urllib.parse
from dotenv import load_dotenv
from .email_Extractor import extract_emails
from utils.logger import log_error
import os
import re

load_dotenv()

API_KEY = os.getenv('GOOGLE_API_KEY')
CX = os.getenv('GOOGLE_CX')

def search_google(query):
    """Function to search Google using Custom Search API."""
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://www.googleapis.com/customsearch/v1?q={encoded_query}&key={API_KEY}&cx={CX}"

    try:
        response = requests.get(url)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        log_error(str(e))
        return None

def is_valid_website(link):
    """Check if the link is a valid website."""
    website_pattern = r"https?://(?:www\.)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}"
    return re.match(website_pattern, link) is not None

def enrich_data(item):
    """Enrich the data by analyzing the website presence and other details."""
    title = item.get('title', 'N/A')
    link = item.get('link', 'N/A')
    snippet = item.get('snippet', 'N/A')

    has_website = is_valid_website(link)

    emails = extract_emails(snippet)

    website_status = "Has Website" if has_website else "No Website"
    
    return {
        "title": title,
        "link": link,
        "snippet": snippet,
        "emails": ', '.join(emails) if emails else 'No emails found',
        "website_status": website_status,
    }

def scrape_data(query):
    """Main function to scrape data using the Google Custom Search API."""
    data = search_google(query)
    
    if not data:
        return []
    
    enriched_data = []
    for item in data.get('items', []):
        enriched_item = enrich_data(item)
        enriched_data.append(enriched_item)
    
    return enriched_data
