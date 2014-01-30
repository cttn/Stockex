"""A wrapper for the Yahoo! Finance API."""

import http.client, urllib
import simplejson as json


class YahooStock:
    
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
