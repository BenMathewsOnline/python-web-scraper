# Chat-GPT 4 News Article Web Scraper

This Python script scrapes Google News for article titles related to Chat-GPT 4. The script uses the `requests` and `BeautifulSoup` libraries to extract article titles from the search results.

## Dependencies

- Python 3.x
- requests
- beautifulsoup4

## Installation

1. Install Python 3.x from the official website: https://www.python.org/downloads/

2. Install the required libraries using pip:

```bash
pip install requests
pip install beautifulsoup4

Usage

Run the script in Visual Studio Code or any other Python-compatible IDE.

bash
python web_scraper.py
The script will search Google News for articles about "Chat-GPT 4" and print the titles of the articles found on the first page of the search results.
You can adjust the pages parameter in the get_article_titles function to search more pages of results.

Disclaimer

Web scraping can be against the terms of service for some websites. Always make sure to review the website's terms and conditions, and respect any limitations or guidelines they provide. Use this script responsibly and at your own risk.
