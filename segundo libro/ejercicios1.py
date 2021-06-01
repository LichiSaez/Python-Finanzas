import pandas as pd
data = pd.read_excel('AAPL.xlsx', sheet_name='Hoja1')
data['var_diaria'] = 100*((data.close - data.open))/ data.open
pd.options.display.precision = 2
pd.options.display.max_rows = 4
print(data)

data.to_excel('AAPL_ej.xlsx',sheet_name='Ej3',columns=["timestamp","var_diaria"])