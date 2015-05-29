"""Module to run tests
"""
from unittest import TestCase

from stockex import stockwrapper as sw

class TestStockex(TestCase):

    def setUp(self):
        self.data = sw.YahooData()

    def tearDown(self):
        pass

    def test_get_historical(self,):

        result = self.data.get_historical('YHOO',['Open','Close','High','Low'],startDate='2014-09-11',endDate='2015-02-10',limit=5)
        print(result)
