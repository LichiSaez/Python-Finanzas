maxPerdida = 5

if maxPerdida > 1 and maxPerdida <= 15:
    if maxPerdida > 8:
        tipo = "Stop Largo"
    elif maxPerdida > 6:
        tipo = "Stop SemiLargo"
    elif maxPerdida > 3:
        tipo = "Stop Standar"
    elif maxPerdida > 1:
        tipo = "Stop Corto"
else:
    tipo = "Fuera de rango"
print(tipo)