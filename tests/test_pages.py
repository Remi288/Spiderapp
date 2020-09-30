import unittest
from src.db import DB
from src.db.pages import Pages

class TestPages(unittest.TestCase):

  def setUp(self) -> None:
    self.pages = Pages(DB.new_connect())


  def test_select(self):
    DB().setup()
    DB().seed()
    result = [(1, 'https://www.facebook.com'), (2, 'https://rb.gy/zd2xxz')]
    self.assertEqual(self.pages.select(), result)



  def test_fetch_url(self):
    DB().setup()
    DB().seed()
    result = [('https://rb.gy/zd2xxz',)]
    self.assertEqual(self.pages.fetch_url(2), result)



  def test_find(self):
    DB().setup()
    DB().seed()
    result = [(1, 'https://rb.gy/zd2xxz')]
    self.assertEqual(self.pages.find(1)[:2], result)


  def test_update_id(self):
    DB().setup()
    DB().seed()
    result = [(1, 'https://rb.gy/zd2xxz', True)]
    self.assertEqual(self.pages.find(1)[:3], result)


  def tearDown(self) -> None:
    self.pages = None

    
  if __name__ =='__main__':
    unittest.main()
