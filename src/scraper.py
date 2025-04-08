import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()

