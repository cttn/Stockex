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
        self.stock = sw.YahooData()

    def tearDown(self):
        pass

    def test_enquire(self, ):
        data = self.stock.enquire('SELECT * FROM yahoo.finance.quote WHERE symbol IN ("FRAN.BA")')
        logging.debug(data)

    def test_get_current(self,):
        data = self.stock.get_current("BMA.BA")
        logging.debug(data)

    def test_get_news_feed(self,):
        data = self.stock.get_news_feed("FRAN.BA")
        logging.debug(data)

    def test_get_options_info(self,):
        data = self.stock.get_options_info('C')
        logging.debug(data)

    def test_get_index(self,):
        data = self.stock.get_index('DJI')
        logging.debug(data)

    def test_get_industry_ids(self,):
        data = self.stock.get_industry_ids()
        logging.debug(data)

    def test_get_industry_index(self,):
        data = self.stock.get_industry_index('914')
        logging.debug(data)

    def test_get_historical(self,):
        logging.debug("with full list of params")
        data = self.stock.get_historical(
                'YHOO',
                ['Open', 'Close', 'High', 'Low'],
                startDate='2014-09-11',
                endDate='2015-02-10',
                limit=5)
        logging.debug(data)
        logging.debug("only with symbol")
        data = self.stock.get_historical('YHOO')
        logging.debug(data)
