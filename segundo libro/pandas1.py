import pandas as pd

##pd.options.display.max_rows = 4
##pd.options.display.precision = 2
##data = pd.read_csv('AAPL.csv', sep=",")
##print(data)
##data = pd.read_excel('AAPL.xlsx', sheet_name="Hoja1", index_col="timestamp")
data = pd.read_excel('AAPL.xlsx', sheet_name="Hoja1")
columnas = ["timestamp", "open", "close"]
##data = pd.read_excel('AAPL.xlsx', sheet_name="Hoja1", index_col="timestamp", usecols=columnas)
##print(data)
##print(data.info())
print(data.shape)
print(data.columns)
print(list(data.columns))
print(data.dtypes)
print(dict(data.dtypes))    