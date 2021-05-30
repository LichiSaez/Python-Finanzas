import pandas as pd
data = pd.read_excel('AAPL.xlsx', sheet_name='Hoja1')
copia = data[['timestamp','open','close']].copy().set_index("timestamp")
# ? dos maneras de hacer lo mismo con .copy() y con .filter([])
copia = data.filter(['timestamp', 'open', 'close']).set_index("timestamp")
#? inverso con .drop
copia = data.drop(['high','low', 'adjusted_close'], axis=1)
print(copia.head())