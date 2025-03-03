import requests
from bs4 import BeautifulSoup

def scrape_promtior_website(url="https://promtior.ai/"):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status codes
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Remove script and style tags to avoid JavaScript/CSS noise
        for script in soup(["script", "style", "nav", "footer"]):
            script.decompose()
        
        # Extract text from main content (adjust tags based on website structure)
        main_content = soup.find("main") or soup.find("body")
        website_text = main_content.get_text(separator="\n", strip=True)
        return website_text
    except Exception as e:
        print(f"Scraping failed: {e}")
        return ""

# Save the scraped text to a file
website_text = scrape_promtior_website()
with open("data/website_text.txt", "w", encoding="utf-8") as f:
    f.write(website_text)