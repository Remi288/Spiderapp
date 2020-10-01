import unittest
from src.db import DB
from src.db.links import Links

class TestLinks(unittest.TestCase):
  ''' class that test for link class
  insert test for the insert function to insert extracted url
  '''


  def setUp(self) -> None:
    self.links = Links(DB.new_connect())


  def test_insert(self):
    DB().setup()
    DB.seed()
    self.assertEqual(self.links.insert(1,2, 'https://www.wikipedia.com'), None)


  def test_select(self):
    DB().setup()
    DB.seed()
    self.links.insert(1,2, 'https://www.wikipedia.com')
    result = [(1, 'https://www.wikipedia.com')]
    self.assertEqual(self.links.select(1), result)


  def test_delete(self):
   DB.setup()
   DB.seed()
   self.links.insert(1,2, 'https://www.wikipedia.com')
   self.links.delete()
   self.assertEqual(self.links.select(1), [])


  def tearDown(self) -> None:
    self.links.delete()
    self.links = None