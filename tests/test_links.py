import unittest
from src.db import DB
from src.db.links import Links

class TestLinks(unittest.TestCase):


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
    self.assertEqual(self.links.select(), result)


  def test_delete(self):
   DB.setup()
   DB.seed()
   self.links.insert(1,2, 'https://www.wikipedia.com')
   self.links.delete()
   self.assertEqual(self.links.select(), [])


  def tearDown(self) -> None:
    self.links.delete()
    self.links = None