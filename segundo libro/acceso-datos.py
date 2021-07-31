import pandas as pd 
pd.options.display.max_rows = 8
data = pd.read_excel('AAPL.xlsx', sheet_name='Hoja1')
dataIndiceFecha = data.set_index("timestamp")
#?print(dataIndiceFecha.loc["2020-03-04"])
#print(dataIndiceFecha.iloc[2])
#print(data.iloc[[2,4]])
#print(data.loc[2:4])
#print(data.iloc[2:4])
#?print(dataIndiceFecha.loc["2020-03-04" : "2020-03-01"])
#? todo = data.iloc[:]

print(data.loc[:,['timestamp','close']])
print(data.loc[0:2, ['timestamp','close','volume']])
print(data.iloc[0:2,[0,4,6]])
print(data.tail(3).loc[::-1,['timestamp', 'close', 'volume']])
print(data[0:20:3])
data = data.loc[::-1].reset_index(drop=False)
print(data)
