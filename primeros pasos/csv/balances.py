import csv
data = csv.reader(open('primeros pasos\csv\\balances.csv'), delimiter = ';')

balances = list()
for fila in data:
    if fila[0] == "FB":
        balances.append(fila)
print("La cantidad de balances es ", len(balances), "\nEl primero es ", balances[0])

activos_anuales = {}
for balance in balances:
    if balance[1] == "anual":
        activos_anuales[balance[2]] = round(int(balance[7]) / 1000000)
print(activos_anuales)

ratio = {}
for balance in balances:
    if balance[1] == "anual":
        try:
            ratio[balance[2]] = round(int(balance[16]) / int(balance[13]), 2)
        except:
            ratio[balance[2]] = "No se pudo calcular"
print(ratio)

