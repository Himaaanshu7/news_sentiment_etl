import os
import requests
import datetime
import pandas as pd
from bs4 import BeautifulSoup

def extract_headlines():
    url = "https://www.reuters.com/world/"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/114.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("❌ Failed to fetch page:", response.status_code)
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.select('a[data-testid="Heading"]')

    headlines = []
    for article in articles:
        title = article.get_text(strip=True)
        href = article.get('href')
        link = f"https://www.reuters.com{href}" if href and href.startswith('/') else href
        headlines.append({
            "title": title,
            "url": link,
            "date": datetime.datetime.utcnow().isoformat()
        })

    df = pd.DataFrame(headlines)
    # ✅ Save to data/headlines_raw.csv (simplified)
    output_path = os.path.join("data", "headlines_raw.csv")
    os.makedirs("data", exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"✅ Saved {len(df)} headlines to {output_path}")
    return df

