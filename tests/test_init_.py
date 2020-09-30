import unittest
from src.db import DB


class TestDb(unittest.TestCase):
  '''class that tests db class in _init_.py'''

  def setUp(self):
    '''function that sets up for testing '''
    self.db = DB()


  def test_connect(self):
    '''function that tests the connect function'''
    connection_object = self.db.connect()
    self.assertIsNotNone(connection_object)

  def test_new_connect(self):
    '''function that tests the new_connect function'''
    connection_object = self.db.new_connect()
    self.assertIsNotNone(connection_object)

  def test_setup(self):
    '''function that tests the setup function'''
    self.assertEqual(self.db.setup(), None)
    cursor = self.db.new_connect().cursor()
    query=cursor.execute('SELECT url FROM pages WHERE id=1 ')
    self.assertEqual(query, None)

  def test_seed(self):
    '''function that tests the seed function'''
    # self.db.setup()
    # seed = self.db.seed()
    # self.assertIsNotNone(seed)


  def tearDown(self):
    self.db = None

if __name__ == '_main_':
    unittest.main()