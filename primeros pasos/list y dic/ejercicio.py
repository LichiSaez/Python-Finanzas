# listado = [1,2,3,4,5,6,7,8,9,10,11,12]
# print(listado[1::2])
# print(listado[4::])
# print(listado[5:10])
# print(listado[1:-3:2])
# print(listado[-1::-3])
# print(sum(listado)/len(listado))
import random

# lideres = ["GGAL","PAMP","YPFD","TECO2","EDN","LOMA","BBAR"]
# galpones = ["AGRO","FIPL","MIRG","GARO","LONG"]

# lideres.append(galpones[1])
# print(lideres)

# lideres.insert(4,galpones[4])
# print(lideres)

# galponx3 = random.sample(galpones, 3)
# lideres[random.randrange(0,5)] = galponx3
# print(lideres)

panel = {'ALUA': 29.35, 'BBAR': 120.85, 'BMA': 265.2, 'BYMA': 290, 'CEPU': 29, 'COME': 3, 'CRES': 40.7}

azar1 =random.uniform(-1,1)
panel['BBAR'] = round(panel['BBAR'] + azar1, 2)
print(panel)
banda = 0.03 * panel['BBAR']
azar3 =random.uniform(-banda,banda)
panel['BBAR'] = round(panel['BBAR'] + azar3, 2)
print(panel)

tickers = panel.keys()
print(random.choice(list(tickers)))

keys = list(panel.keys())
random.shuffle(keys)
listaReordenada = [(key, panel[key]) for key in keys]
print(dict(listaReordenada))

keys = list(panel.keys())
keys.sort()
keys.reverse()
listaReordenada = [(key, panel[key]) for key in keys]
print(dict(listaReordenada))