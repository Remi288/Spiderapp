import unittest


def hello_world():
  return 'hello world'


class MyFirstTests(unittest.TestCase):

  def test_hello(self):        
    self.assertEqual(hello_world(), 'hello world')