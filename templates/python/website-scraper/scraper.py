'''
Docs for BeautifulSoup module: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
First make sure to run 'pip install -r requirements.txt'
'''
from bs4 import BeautifulSoup
import requests

def scrape_website(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_all_hrefs(soup):
    all_hrefs = [link.get('href') for link in soup.find_all('a')]
    return all_hrefs

soup = scrape_website('https://www.python.org/')
all_hrefs = get_all_hrefs(soup)
print(all_hrefs)