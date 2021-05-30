import pandas as pd
data = pd.read_excel('AAPL.xlsx', sheet_name="Hoja1")

data['mov_intra'] = data.close - data.open
data = data.drop(["high","low","adjusted_close"], axis=1).head()
print(data)

data.to_excel('AAPL_Modificado1.xlsx', sheet_name='HojaEjemplo')