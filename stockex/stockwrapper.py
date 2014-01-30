"""A wrapper for the Yahoo! Finance API."""

import http.client, urllib
import simplejson as json


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

    def enquire(self,yql):
        """Execute YQL query to Yahoo! API"""

        conn = http.client.HTTPConnection('query.yahooapis.com')
        string_query = urllib.parse.urlencode(
                {'q': yql, 'format': 'json', 'env': self.DATATABLES_URL}
                )
        conn.request('GET', self.PUBLIC_API_URL + '?' + string_query)
        return json.loads(conn.getresponse().read())

    def _format_symbol_list(self, symbol_list):
        """Gives the proper format for a YQL to a symbol list"""
        return ','.join(["\""+symbol+"\"" for symbol in symbol_list])

    def _validate_response(self, response, tag):
        pass

    def get_current(self, symbol_list, columns = None, validate = None):
        """Retrieves the latest data (with some delay depending on the
        country/market) for the list of symbols given in symbol_list"""

        if columns is None:
            columns = '*'

        _formatted_columns = ','.join(columns)
        _formatted_symbols = self._format_symbol_list(symbol_list)

        yql = 'SELECT %s FROM %s WHERE symbol IN (%s)' \
            %(_formatted_columns, self.FINANCE_TABLES['quotes'], _formatted_symbols)

        _response = self.enquire(yql)
        
        if validate:
            return self._validate_response(self, _response, 'quote')
        else:
            return _response
