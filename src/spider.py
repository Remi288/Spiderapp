import requests
import re
from bs4 import BeautifulSoup
from src.schemas.celery import app

@app.task
def get_url(url):
  request = requests.get(url)
  # print(re)
  soup = BeautifulSoup(request.content, 'html')
  links_list = []
  for link in soup.find_all('a', href=True):
    links = link['href']
    if re.search("^https", links):
      links_list.append(links)
  return links_list[:10]


print(get_url('https://www.facebook.com'))