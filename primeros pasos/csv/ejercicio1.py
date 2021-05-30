import csv
data = csv.reader(open('primeros pasos\csv\\SPY.csv'), delimiter=';')

lista = []
for fila in data:
    lista.append(fila)

cierres_ajustados = [lista[i][5] for i in range(1, len(lista))]
variacionesPos = []
variaciones = []
for i in range(0, len(cierres_ajustados)):
    try:
        var = round((float(cierres_ajustados[i])/float(cierres_ajustados[i+1]) - 1)*100, 2)
        variaciones.append(var)
    except:
        var = 0
    if var > 5:
        variacionesPos.append(var)
print(len(variacionesPos))
#? Usamos range(2) para ajustarse a esta situación particular(ver línea 44)
cierres = [lista[i][4] for i in range(2, len(lista))]
aperturas = [lista[i][1] for i in range(1, len(lista))]
gaps = []

for i in range(0, len(aperturas)):
    try:
        gap = round((float(aperturas[i])/float(cierres[i]) - 1) * 100, 2)
    except:
        gap = 0
    gaps.append(gap)
print(gaps[0:5])

gap_pos, gap_neg, gap_neutros = ([] for i in range(3))
for gap in gaps:
    if gap > 0:
        gap_pos.append(gap)
    elif gap < 0:
        gap_neg.append(gap)
    else:
        gap_neutros.append(gap)
print("Gaps Positivos: ", len(gap_pos), "Gaps Negativos: ",len(gap_neg), "Gaps Neutros: ", len(gap_neutros))

intras, intras_pos, intras_neg, intras_neutros = ([] for i in range(4))
#! Redefinimos el rango de cierres para que no de problemas y se ajuste a todas las cituaciones
cierres = [lista[i][4] for i in range(1, len(lista))]
for i in range(0, len(aperturas)):
    try:
        intra = round((float(cierres[i])/float(aperturas[i]) - 1) * 100, 2)
        if intra > 0:
            intras_pos.append(intra)
        elif intra < 0:
            intras_neg.append(intra)
        else:
            intras_neutros.append(intra)
        intras.append(intra)
    except:
        intra = 0
print("Intras Positivos: ", len(intras_pos), "Intras Negativos: ", len(intras_neg), "Intras Neutros: ", len(intras_neutros))

dic = {}
dic.update({"GapsPos Media" : round(sum(gap_pos)/len(gap_pos),2)})
dic.update({"GapsNeg Media" : round(sum(gap_neg)/len(gap_neg),2)})
dic.update({"GapsPos %" : round(100*len(gap_pos)/len(gaps), 2)})
dic.update({"GapsNeg %" : round(100*len(gap_neg)/len(gaps), 2)})
dic.update({"GapsNeutros %" : round(100*len(gap_neutros)/len(gaps), 2)})

dic.update({"IntrasPos Media" : round(sum(intras_pos)/len(intras_pos),2)})
dic.update({"IntrasNeg Media" : round(sum(intras_neg)/len(intras_neg),2)})
dic.update({"IntrasPos %" : round(100*len(intras_pos)/len(intras), 2)})
dic.update({"IntrasNeg %" : round(100*len(intras_neg)/len(intras), 2)})
dic.update({"IntrasNeutros %" : round(100*len(intras_neutros)/len(intras), 2)})
print(dic)

vars_pos, vars_neg, vars_neutros = ([] for i in range(3))
for var in variaciones:
    if var > 0:
        vars_pos.append(var)
    elif var < 0:
        vars_neg.append(var)
    else:
        vars_neutros.append(var)
dv = {}
dv.update({"VarPos Media" : round(sum(vars_pos)/len(vars_pos), 2)})
dv.update({"VarNegs Media" : round(sum(vars_neg)/len(vars_neg), 2)})
dv.update({"VarPos %" : round(100*len(vars_pos)/len(variaciones), 2)})
dv.update({"VarNegs %" : round(100*len(vars_neg)/len(variaciones), 2)})
dv.update({"VarNeutros %" : round(100*len(vars_neutros)/len(variaciones), 2)})
print(dv)