import pandas as pd
data = pd.read_excel('AAPL.xlsx', sheet_name="Hoja1")

for i in range(len(data)):
    if data.loc[i,'close'] >= data.loc[i,'open']:
        data.loc[i,'color_vela'] ="verde"
    else:
        data.loc[i,'color_vela'] = "rojo"
data = data.drop(["high", "low"], axis=1).head(8)
print(data)
