import csv
data = csv.reader(open('primeros pasos\csv\SPY.csv'), delimiter = ';')
lista = []
for fila in data:
    lista.append(fila)

# fechas = []
# for i in range(1, len(lista)):
#     fechas.append(lista[i][0])
#? Manera abreviada:
fechas = [lista[i][0] for i in range(1, len(lista))]
print(fechas[0:5])