import pytz
import datetime as dt
from datetime import datetime as dt_dt
from datetime import date as dt_date
hoy = dt_dt.today()
print(hoy)
expiracion_str = "2021-04-17"
expiracion = dt_dt.strptime(expiracion_str, '%Y-%m-%d' )
print(expiracion)
print(expiracion - hoy)
dias = (expiracion - hoy).days
segundos = (expiracion - hoy).seconds
print(F"Días restantes {dias}\nSegundos restantes: {segundos}")

año = 2020
mes= 12
dia= 24
hora = 20
minutos = 59
segundos = 59
fecha = dt_dt(año,mes,dia,hora,minutos,segundos)
print(fecha, fecha.ctime())
hoy_txt = dt_dt.strftime(hoy, "%d %B %Y")
print(hoy_txt)
hoy = dt_dt.now()
hoy_berlin = hoy.astimezone(pytz.timezone('Europe/Berlin'))
print(hoy)
print(hoy_berlin)