import pandas as pd
#? creando con dos variables distintas
# data = [["ALUA",19.15],["BBAR",73.70],["BMA",144.4],["BYMA",234]]
# tabla = pd.DataFrame(data, columns=['Ticker','Precio'])
#? creando con diccionario
# data = {
#     'Tickers':['ALUA','BBAR','BMA','BYMA'],
#     'Precios': [19.15,73.7,144.4,234]
#     }
# tabla = pd.DataFrame(data, 
# ? poniendole index personalizado
# index=["act1","act2","act3","act4"])
# ? creando con lista de diccionario
data = [
    {"ticker": "ALUA", "Precio": 19.15, "Tipo": "Accion"},
    {"ticker": "BBAR", "Precio": 73.7, "Tipo": "Accion"},
    {"ticker": "BMA", "Precio": 144.4},
    {"ticker": "BYMA", "Precio": 234, "Tipo": "Accion"}
]
# tabla = pd.DataFrame(data)
# ? seleccionar columnas
tabla = pd.DataFrame(data, columns=["ticker", "Precio"])
print(tabla)