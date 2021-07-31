import pandas as pd

data = pd.read_excel('AAPL.xlsx')
data.set_index('timestamp', inplace=True)
data = data[::-1]
##print(data.loc["2000-03-26" : "2000-04-02"])
#? Paso todo junto
print(data[data['volume']>50000000].loc[data['close']<100])
#? Paso separado
filtro1 = data[data['volume']>50000000]
filtro2 = data[data['close']<100]
filtro = filtro1.merge(filtro2, how="inner")
#? Paso con operadores lógicos
filtro = data[(data['volume']>50000000) & (data['close']<100)]
print(filtro)
#? El operador OR se hace con | o how=outer
