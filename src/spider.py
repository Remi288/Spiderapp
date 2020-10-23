import requests
import re
from bs4 import BeautifulSoup
from src.db import DB


def spider_scrap(page_id):
  '''function that recieve a page_id and insert links in the link table'''

  page_ids = [i[0] for i in DB().pages().select()]
  if page_id in page_ids:
    url = DB().pages().fetch_url(page_id)
  else:
    raise ValueError('page_id not valid')

  #update is_scraping to true
  DB().pages().update_id_true(page_id)

  #fetch the html content at the page url
  page = requests.get(url[0])





# fetching the html content to extract maximum 10 hyperlinks
  soup = BeautifulSoup(page.text, features='html.parser')
  links_list = []
  for link in soup.find_all('a', href=True):
    links = link['href']
    if re.search("^https", links):
      links_list.append(links)
  link_url = links_list[:10]

  DB.links().delete(page_id)

#saves the newly extratcted links to the database for the page
  for url in link_url:
    DB.links().insert(page_id, url)

  DB().pages().update_id_false(page_id)

# print(spider_scrap(1))