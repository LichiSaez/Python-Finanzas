from datetime import datetime as dt_dt
hoy = dt_dt.now()
año = hoy.year
print(año)

import calendar
import locale
locale.setlocale(locale.LC_TIME,"esp")
dia = 19
mes = 12


fin_año = dt_dt(año,12,31)
dias_faltantes = (fin_año - hoy).days
print(dias_faltantes)