from stockwrapper import YahooData

data = YahooData()

#print(data.enquire('select * from yahoo.finance.quotes where symbol in ("FRAN.BA")'))
print(data.get_current(["BMA.BA", "FRAN.BA"]))
