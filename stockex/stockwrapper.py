"""A wrapper for the Yahoo! Finance API.

 Ex Usage:
    from stockex import stockwrapper as sw
    data = sw.YahooData()
    print(data.get_current('GOOG')) 
"""

import http.client, urllib
import json


class YahooData:
    
    PUBLIC_API_URL = 'http://query.yahooapis.com/v1/public/yql'
    DATATABLES_URL = 'store://datatables.org/alltableswithkeys'
    HISTORICAL_URL = 'http://ichart.finance.yahoo.com/table.csv?s='
    RSS_URL        = 'http://finance.yahoo.com/rss/headline?s='
    FINANCE_TABLES = {'quotes': 'yahoo.finance.quotes',
                      'options': 'yahoo.finance.options',
                      'quoteslist': 'yahoo.finance.quoteslist',
                      'sectors': 'yahoo.finance.sectors',
                      'industry': 'yahoo.finance.industry'
                      }

    class Error(Exception):

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return repr(self.value)


    def enquire(self, yql):
        """Execute YQL query to Yahoo! API"""

        conn = http.client.HTTPConnection('query.yahooapis.com')
        string_query = urllib.parse.urlencode(
                {'q': yql, 'format': 'json', 'env': self.DATATABLES_URL}
                )
        conn.request('GET', self.PUBLIC_API_URL + '?' + string_query)
        return json.loads(conn.getresponse().read().decode('utf-8'))

    def _format_symbol_list(self, symbol_list):
        """Gives the proper format for a YQL to a symbol list"""
        return ','.join(["\""+symbol+"\"" for symbol in symbol_list])

    def _validate_response(self, response, tag):
        if response:
            is_valid_response = 'query' in response and         \
                            'results' in response['query'] and  \
                            tag in response['query']['results']
        
        if is_valid_response:
            quote_info = response['query']['results'][tag]
        elif 'error' in response:
            raise self.Error("YQL failed with error: {0}" .format(response['error']['description']))
        else:
            raise self.Error("YQL response malformed")
        
        return quote_info

    def get_current(self, symbol_list, columns = None):
        """Retrieves the latest data (with some delay depending on the
        country/market) for the list of symbols given in symbol_list"""

        if columns is None:
            columns = '*'

        _formatted_columns = ','.join(columns)
        _formatted_symbols = self._format_symbol_list(symbol_list)

        yql = 'SELECT {0} FROM {1} WHERE symbol IN ({2})' \
            .format(_formatted_columns, self.FINANCE_TABLES['quotes'], _formatted_symbols)

        _response = self.enquire(yql)
        return self._validate_response(_response, 'quote')

    def get_historical(self, symbol, columns = None):
        """Retrieves historical data for the provided stock 'symbol'.
        Default columns are: date, open, close, high, low, volume and
        adjusted close."""

        if columns is None:
            _formatted_columns = '\"Date,Open,High,Low,Close,Volume,AdjClose\"'
        else:
            _formatted_columns = ','.join(columns)

        yql = 'SELECT * FROM csv WHERE url=\'{0}\' AND columns=' \
             .format(self.HISTORICAL_URL + symbol) + _formatted_columns

        _response = self.enquire(yql)
        _formatted_response = self._validate_response(_response, 'row')

        del _formatted_response[0] #delete first row which only contains column names
        return _formatted_response

    def get_news_feed(self, symbol):
        """Retrieves the RSS feed for the provided symbol"""

        feed_url = self.RSS_URL + symbol
        yql = 'SELECT title, link, description, pubDate FROM rss WHERE url=\'{0}\'' \
                .format(feed_url)
        _response = self.enquire(yql)
        _formatted_response = self._validate_response(_response, 'item')
        return _formatted_response

    def get_options_info(self, symbol, expiration = None, columns = None):
        """Retireves options data for the provided symbol"""
    
        if columns is None:
            columns = '*'

        _formatted_columns = ','.join(columns)
        yql = 'SELECT {0} FROM {1} WHERE symbol=\'{2}\''  \
                .format(_formatted_columns, self.FINANCE_TABLES['options'], symbol)

        if expiration is not None:
            yql += " AND expiration =\'{0}\'" .format(expiration)

        _response = self.enquire(yql)
        return self._validate_response(_response, 'optionsChain')

    def get_index(self, index, columns = None):
        """Retrieves data for the stock 'index'."""

        if columns is None:
            _formatted_columns = '*'
        else:
            _formatted_columns = ','.join(columns)

        yql = 'SELECT {0} FROM {1} WHERE symbol=\'@{2}\'' \
                .format(_formatted_columns, self.FINANCE_TABLES['quoteslist'], index)

        _response = self.enquire(yql)
        return self._validate_response(_response, 'quote')

    def get_industry_ids(self):
        """Retrieves all industry names and ids"""

        yql = 'SELECT * FROM {0}' .format(self.FINANCE_TABLES['sectors'])
        _response = self.enquire(yql)
        return self._validate_response(_response, 'sector')


    def get_industry_index(self, iid):
        """Retrieves all symbols of a given industry"""

        yql = 'SELECT * FROM {0} WHERE id=\'{1}\'' \
                .format(self.FINANCE_TABLES['industry'], iid)

        _response = self.enquire(yql)
        return self._validate_response(_response, 'industry')

