import requests
from bs4 import BeautifulSoup

def get_article_titles(query, pages=1):
    titles = []

    for page in range(1, pages + 1):
        url = f"https://www.google.com/search?q={query}&tbm=nws&start={10 * (page - 1)}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        for title in soup.find_all("div", class_="BNeawe vvjwJb AP7Wnd"):
            titles.append(title.get_text())

    return titles

if __name__ == "__main__":
    query = "Chat-GPT 4"
    article_titles = get_article_titles(query)

    print(f"News articles about {query}:")
    for title in article_titles:
        print(f"- {title}")
