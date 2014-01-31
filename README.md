# Stockex

Python 3 wrapper for Yahoo! Finance API.



## Requirements

* Python 3



## Install

> git clone https://github.com/cttn/Stockex.git
>
> cd Stockex
>
> python setup.py install



## Example Usage

```
 from stockex import stockwrapper as sw

 data = sw.YahooData()

 # Print Current data of a Stock
 print(data.get_current("GOOG"))

 # Print historical data of a Stock
 print(data.get_historical("GOOG"))


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



## Credits

Initially based on (python2.7 script) https://github.com/gurch101/StockScraper



