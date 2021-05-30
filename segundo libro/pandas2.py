import pandas as pd
data = pd.read_excel('AAPL.xlsx', sheet_name="Hoja1")
data.set_index('timestamp', inplace=True)
data['precio_medio'] = (data.open + data.close + data.low + data.high) / 4
data = data.drop(["high", "low"], axis=1).head()
data['vol_mln-usd'] = round((data.volume * data.precio_medio)/ 1000000)
data = data.drop(['open','close'], axis=1).head()
print(data)
