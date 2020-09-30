# Show examples of how you would use ALL your implementations here
from src.db import DB



#
# db = DB()
# # db.connect()
# db.new_connect()
# db.setup()
# db.seed()
dd = DB.new_connect()
pages = DB().pages(dd)
# pages.fetch_url(2)
# print(pages.fetch_url(2))