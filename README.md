# Stockex

<!-- [![Build Status](https://travis-ci.org/josuebrunel/Stockex.svg?branch=master)](https://travis-ci.org/josuebrunel/Stockex) -->
[![Coverage Status](https://coveralls.io/repos/josuebrunel/Stockex/badge.svg?branch=master)](https://coveralls.io/r/josuebrunel/Stockex?branch=master)
<!-- [![Code Health](https://landscape.io/github/josuebrunel/Stockex/master/landscape.svg?style=flat)](https://landscape.io/github/josuebrunel/Stockex/master) -->
Python 3 wrapper for Yahoo! Finance API.



## Requirements

* Python 3



## Install

From PYPI:
```shell
pip install stockex
```

From Github:
```shell
git clone https://github.com/cttn/Stockex.git

cd Stockex

python setup.py install
```


## Example Usage

```python
from stockex import stockwrapper as sw

data = sw.YahooData()

# Print Current data of a Stock
print(data.get_current(['GOOG']))

# Print historical data of a Stock, returns data of last week
print(data.get_historical("GOOG"))

# Print historical data of a Stock according to the startDate and endDate
print(data.get_historical('YHOO', ['Open', 'Close', 'High', 'Low'],
                          startDate='2014-09-11', endDate='2015-02-10', limit=5))

# Trivial formatting
print("Google stock: Date and Price")
for item in data.get_historical("GOOG"):
    print(item['Date'] + '\t' + item['Close'])


# Other methods:
 
# Do a custom YQL query to Yahoo! Finance YQL API:
data.enquire('select * from yahoo.finance.quotes where symbol in ("GOOG", "C")')

# Get news feed of a Company
data.get_news_feed("GOOG")

# Get options data
data.get_options_info("GOOG")

# Get industry ids
data.get_industry_ids()

# Get industry index from a given id
data.get_industry_index('914')
```


## Contributing

Contributions of all sorts are welcomed.
Feel free to fork, make pull requests, ask for features, etc.


## Credits

Based on the Python2.7 (Public Domain) script StockScraper: [Code](https://github.com/gurch101/StockScraper) and [Docs](http://www.gurchet-rai.net/dev/yahoo-finance-yql).


## License

Public Domain.

