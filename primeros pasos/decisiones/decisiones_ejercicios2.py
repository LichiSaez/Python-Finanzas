##
activos1 = ["ALUA","BMA","BYMA","CEPU","COME", "CRES","CVH","EDN","GGAL","MIRG"]
activos2 = ["PAM","SUPV","TECO2","TGNNO4","TGSU2","TRAN","TXAR","VALO","YPF"]

activos = activos1 + activos2
print(activos,len(activos))

##
ticker = input("Pedime una variable pibe dale:").upper()
if ticker in activos:
     print("Si pibe, está")
else:
    print("no pibe, ja' de joder")

##
precios = {"GGAL": 80, "YPF": 500}
ticker2 = input("Tirame otro pibe:").upper()
if ticker2 in precios:
    print(f"Si pibe mirá, el precio de {ticker2} es {precios[ticker2]}")
elif ticker2 in activos:
    print(f"Mira pibe, {ticker2} no tiene precio")
else:
    print("No hay nada pibe, mejor tirame la goma")

