import csv
data = csv.reader((open('primeros pasos\csv\\estado_resultados.csv')), delimiter=';')

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