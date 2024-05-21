import requests
from bs4 import BeautifulSoup
import feedparser
import json
import os
from datetime import datetime

# Configuration
TECHMEME_URL = "https://www.techmeme.com/feed.xml"
OTHER_SOURCE_1_URL = "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"
OTHER_SOURCE_2_URL = "https://feeds.bbci.co.uk/news/technology/rss.xml"
OUTPUT_FILE = "news.json"

def fetch_techmeme_news():
    feed = feedparser.parse(TECHMEME_URL)
    news_items = []
    for entry in feed.entries[:5]:  # Fetch top 5 news
        news_items.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })
    return news_items

def fetch_other_source_news(url):
    feed = feedparser.parse(url)
    news_items = []
    for entry in feed.entries[:5]:  # Fetch top 5 news
        news_items.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })
    return news_items

def aggregate_news():
    news_data = {
        'techmeme': fetch_techmeme_news(),
        'source_1': fetch_other_source_news(OTHER_SOURCE_1_URL),
        'source_2': fetch_other_source_news(OTHER_SOURCE_2_URL)
    }
    return news_data

def save_news_to_file(news_data):
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(news_data, f, indent=4)

def main():
    news_data = aggregate_news()
    save_news_to_file(news_data)
    print("News aggregation completed and saved to", OUTPUT_FILE)

if __name__ == "__main__":
    main()
