import pandas as pd 
pd.options.display.max_rows = 8
data = pd.read_excel('AAPL.xlsx', sheet_name='Hoja1')
print(data.loc[2])