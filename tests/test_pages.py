import unittest
from src.db import DB
from src.db.pages import Pages

class TestPages(unittest.TestCase):
  '''test that handle the page class'''

  def setUp(self) -> None:
    self.pages = Pages(DB.new_connect())


  def test_select(self):
    '''test for selection function in pages'''
    DB().setup()
    DB().seed()
    result = [(1, 'https://www.facebook.com'), (2, 'https://rb.gy/zd2xxz')]
    self.assertEqual(self.pages.select(), result)



  def test_fetch_url(self):
    '''test for fetch_url function in pages'''
    DB().setup()
    DB().seed()
    result = ('https://rb.gy/zd2xxz',)
    self.assertEqual(self.pages.fetch_url(2), result)



  def test_find(self):
    ''' test for find function in pages'''
    DB().setup()
    DB().seed()
    result = (1, 'https://www.facebook.com')
    self.assertEqual(self.pages.find(1)[:2], result)


  def test_update_id_true(self):
    '''test for update_id_true function in pages'''
    DB().setup()
    DB().seed()
    result = (1, 'https://www.facebook.com', True)
    self.assertEqual(self.pages.update_id_true(1)[:3], result)

  def test_update_id_false(self):
    '''test for update_id_false function in pages'''
    DB().setup()
    DB().seed()
    result = (1, 'https://www.facebook.com', False)
    self.assertEqual(self.pages.update_id_false(1)[:3], result)


  def tearDown(self) -> None:
    self.pages = None

    
  if __name__ =='__main__':
    unittest.main()
