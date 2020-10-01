# Show examples of how you would use ALL your implementations here
from src.db import DB
from src.spider import spider_scrap
from celery import Celery
from decouple import config


#
db = DB()
db.connect()
db.new_connect()
db.setup()
db.seed()
dd = DB.new_connect()
pages = DB.pages()
# pages.fetch_url(2)
print(pages.fetch_url(2))
print(pages.select())
print(pages.find(2))
# print(pages.update_id(1))
links = DB.links()
# print(links.insert())
# print(links.delete())
print(links.select(1))

app = Celery('main', broker=config('CELERY_BROKER'), backend=config('CELERY_BACKEND'))


@app.task
def scrap_url():
  return spider_scrap(1)




