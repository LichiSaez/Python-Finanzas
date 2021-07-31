import pandas as pd 
pd.options.display.max_rows = 8
data = pd.read_excel('AAPL.xlsx', sheet_name='Hoja1')
dataIndiceFecha = data.set_index("timestamp")
print(dataIndiceFecha.loc["2020-03-04"])
print(dataIndiceFecha.iloc[2])