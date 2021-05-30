import csv
from typing import final 
data = csv.reader((open('primeros pasos\csv\\estado_resultados.csv')), delimiter=';')
estados = [fila for fila in data]

q = 0
respuesta = []
for estado in estados:
    if estado[0] == "AAPL" and estado[1]=="trimestral" and q < 4:
        respuesta.append(round(int(estado[10])/1000000))
        q = q+1
print(respuesta)

empresas = ["FB","AMZN","AAPL", "NFLX", "GOOGL"]
calculado = {}
for empresa in empresas:
    calculado[empresa] = False

screener = {}

for estado in estados: 
    empresa = estado[0]
    if empresa in empresas and estado[1] == "anual" and calculado[empresa] == False:
        try:
            screener[empresa] = round(int(estado[21])/int(estado[19]), 2)
        except:
            screener[empresa] = "No se puede calcular"
        finally:
            calculado[empresa] = True
print(screener)

empresas = [estado[0] for estado in estados]
calculado = {}
for empresa in empresas:
    calculado[empresa] = False
screener = {}

for estado in estados:
    empresa = estado[0]
    if estado[1] == "anual" and calculado[empresa] == False:
        try:
            ratio = round(int(estado[21])/int(estado[19]), 2)
            rd_bln = int(estado[3]) / 1000000000
            if ratio < 0.5 and rd_bln > 5:
                screener[empresa] = ratio
        except:
            ratio = "No se puede calcular"
        finally:
            calculado[empresa] == True
print(screener)


