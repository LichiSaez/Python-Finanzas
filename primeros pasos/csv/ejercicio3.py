import csv
data = csv.reader((open('primeros pasos\csv\\estado_resultados.csv')), delimiter=';')
estados = [fila for fila in data]
rd_lista = []

for estado in estados:
    empresa = estado[0]
    if estado[1] == "trimestral" and empresa == "AAPL":
        try:
            rd_bln = int(estado[3]) / 1000000000
            rd_lista.append(rd_bln)
        except:
            pass
rd_promedio = sum(rd_lista) / len(rd_lista)
print(rd_promedio)



estados = [fila for fila in data]
empresas = [estado[0] for estado in estados]

calculado = {}
for empresa in empresas:
    calculado[empresa] = False
listado = []

for estado in estados:
    empresa = estado[0]
    if estado[1] == "anual" and calculado[empresa] == False:
        try:
            rd_bln = int(estado[3]) / 1000000000
            calculado[empresa] = True
            if rd_bln > 1:
                listado.append(rd_bln)
        except:
            pass
print(len(listado))