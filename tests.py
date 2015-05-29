"""Module to run tests
"""
from unitttest import TestCase

from stockex import stockwrapper as sw

class TestStockex(TestCase):

    def setUp(self):
        data = sw.YahooData()

    def tearDown(self):
        pass

    def test_get_historical(self,):

        result = get_historical('YHOO',['Open','Close','High','Low'],startDate='2014-09-11',endDate='2015-02-10',limit=5)
        print(result)
