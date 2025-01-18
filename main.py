# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import os

# # Initialize Selenium WebDriver
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Run in headless mode to avoid opening a browser
# driver = webdriver.Chrome(options=options)

# # List of company URLs
# company_urls = [
#     "https://www.crunchbase.com/organization/openai",
#     "https://www.crunchbase.com/organization/anthropic",
#     "https://www.crunchbase.com/organization/perplexity",
#     "https://www.crunchbase.com/organization/european-investment-bank",
#     "https://www.crunchbase.com/organization/xai"
# ]

# # Directory to save HTML files
# output_dir = "scraped_pages"
# os.makedirs(output_dir, exist_ok=True)

# # Function to scrape and save HTML
# def scrape_and_save(url):
#     try:
#         driver.get(url)
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.TAG_NAME, "body"))
#         )
#         time.sleep(3)  # Allow time for all dynamic content to load
#         page_source = driver.page_source

#         # Extract company name from URL for file naming
#         company_name = url.split("/")[-1]
#         file_path = os.path.join(output_dir, f"{company_name}.html")

#         # Save HTML to file
#         with open(file_path, "w", encoding="utf-8") as file:
#             file.write(page_source)
#         print(f"Saved {company_name}.html")
#     except Exception as e:
#         print(f"Error scraping {url}: {e}")

# # Iterate through company URLs and scrape
# for url in company_urls:
#     print(f"Scraping data for: {url}")
#     scrape_and_save(url)

# # Quit the driver
# driver.quit()
# print("Scraping completed!")



import csv
from scraper.google_search import scrape_data
import os

QUERY = 'business email addresses for tech influencers'
OUTPUT_FILE = 'data/enriched_tech_influencer_emails.csv'

def save_to_csv(data):
    """Save enriched data to CSV file."""
    if not data:
        print("No data to save.")
        return

   
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "link", "snippet", "emails", "website_status"])
        writer.writeheader()
        writer.writerows(data)

def main():
    """Main function to orchestrate scraping and saving data."""
    print("Starting data scraping and enrichment...")
    enriched_data = scrape_data(QUERY)

    if enriched_data:
        print(f"Found {len(enriched_data)} enriched records. Saving to {OUTPUT_FILE}...")
        save_to_csv(enriched_data)
    else:
        print("No data found to enrich.")
    
    print("Process completed.")

if __name__ == "__main__":
    main()
