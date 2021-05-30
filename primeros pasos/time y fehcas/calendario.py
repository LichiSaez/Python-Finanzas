import calendar 
año = 2021
s_hor = 1
s_ver = 1
calle = 3
mxf = 3
diciembre = 12
calendar.prcal(año, s_hor, s_ver, calle, mxf)
calendar.prmonth(año, diciembre)
print(calendar.isleap(2021))
dia = calendar.weekday(2021,12,19)

import locale
locale.setlocale(locale.LC_TIME,"en")
print(calendar.day_name[dia])

locale.setlocale(locale.LC_TIME,"esp")
print(calendar.day_name[dia])
