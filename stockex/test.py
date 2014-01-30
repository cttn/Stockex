from stockwrapper import YahooStock

data = YahooStock()

print(data.enquire('select * from yahoo.finance.quotes where symbol in ("FRAN.BA")'))
