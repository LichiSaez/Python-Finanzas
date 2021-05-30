import csv
data = csv.reader(open('primeros pasos\csv\SPY.csv'), delimiter = ';')

cierres_aj = [fila[5] for fila in data]
del(cierres_aj[0])

variaciones = []
for i in range(0, len(cierres_aj)):
    try:
        var = round((float(cierres_aj[i])/float(cierres_aj[i+1]) -1)*100, 2)
        variaciones.append(var)
    except:
        pass
print(variaciones[0:4])
