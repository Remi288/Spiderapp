import unittest
from src.spider import spider_scrap

class TestSpider(unittest.TestCase):
  ''' test for the spider'''

  def test_spider_scrap_pagedid_one(self):
    self.assertIsNone(spider_scrap(1))


  def test_spider_scrap_pagedid_two(self):
    self.assertIsNone(spider_scrap(2))

  def test_spider_scrap_pageid_string(self):
    '''test that handle any other type input'''
    with self.assertRaises(ValueError):
      self.assertEqual(spider_scrap('5'), None)