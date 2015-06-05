"""Module to run tests
"""
import logging
from unittest import TestCase
from stockex import stockwrapper as sw

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s %(levelname)s]" +
                    "[%(name)s.%(module)s.%(funcName)s] %(message)s \n")
logging.getLevelName('TestStockex')


class TestStockex(TestCase):

    def setUp(self):
        self.data = sw.YahooData()

    def tearDown(self):
        pass

    def test_get_historical(self,):
        logging.debug("with full list of params")
        result = self.data.get_historical(
                'YHOO',
                ['Open', 'Close', 'High', 'Low'],
                startDate='2014-09-11',
                endDate='2015-02-10',
                limit=5)
        logging.debug(result)
        logging.debug("only with symbol")
        result = self.data.get_historical('YHOO')
        logging.debug(result)
