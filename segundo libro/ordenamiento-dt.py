import pandas as pd

data = pd.read_excel('AAPL.xlsx')
ordenado = data.sort_values(by='adjusted_close',ascending=True)
#print(ordenado.head(8))
data.adjusted_close = round(data.adjusted_close,2)
ordenado = data.sort_values(by=['adjusted_close','volume'], ascending=[True,True])
#print(ordenado.head(8))
vol = data.volume
print(vol)