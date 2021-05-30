import csv
data = csv.reader(open('primeros pasos\csv\\balances.csv'), delimiter = ';')
balances = [fila for fila in data]
empresas = ["AAPL", "AMZN", "FB", "TSLA", "KO", "NFLX"]
screener = {}

##! Poca eficiencia
# for empresa in empresas:
#     for balance in balances:
#         if balance[0] == empresa and balance[1] == "anual":
#             try:
#                 screener[empresa] = round(int(balance[16]) / int(balance[13]), 2)
#             except:
#                 screener[empresa] = "No se pudo calcular"
#             break
# print(screener)

calculado = {}
for empresa in empresas:
    calculado[empresa] = False

for balance in balances:
    empresa = balance[0]
    if empresa in empresas and balance[1] == "anual" and calculado[empresa] == False:
        try:
            screener[empresa] = round(int(balance[16]) / int(balance[13]), 2)
        except:
            screener[empresa] = "No se pudo calcular"
        finally:
            calculado[empresa] = True
print(screener)
