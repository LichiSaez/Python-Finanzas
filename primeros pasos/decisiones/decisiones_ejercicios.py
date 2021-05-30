smaFast = 100
smaSlow = 98
buyPrice = 106
price = 128

trend = smaFast > smaSlow * 1.02
stopLoss = price < buyPrice * 0.95 and price < smaSlow
takeProfit = price > 1.2 * buyPrice or (price > 1.1 * buyPrice and price > smaFast * 1.2)

hold = trend and not stopLoss and not takeProfit
print(price,hold)

if hold: 
    state = "Seguimos invertidos"
else:
    if stopLoss:
        state = "Salimos por stopLoss"
    else:
        state = "Salimos por toma de ganancias"
print(state)

##
cartera = {"AAPL": 30, "AMZN": 25, "NFLX": 20, "FB": 10, "KO": 5, "USD": 10}
ticket = input("Ingrese el activo que quiere saber su % de ponderación: ").upper()

try:
    print(f"La ponderación de {ticket} en su cartera es de {cartera[ticket]} %")
except:
    print("Ingresaste cualquier verdura man")

