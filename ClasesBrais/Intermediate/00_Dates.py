### Dates ###

from datetime import datetime

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


# Leer la fecha actual
now = datetime.now()
print_date(now)

# Hora UNIX desde 1-1-1970
timestamp = now.timestamp()
#print_date(timestamp)

year_2023 = datetime(2023,1,1) # Obligatorios año, mes y día, opcionales hora, minutos, segundos y milisegundos
print_date(year_2023)


from datetime import time

current_time = time(8,50,30) # puedo definir un time en blanco como time() y obtengo 00:00:00
print(current_time.hour)
print(current_time.minute)
print(current_time.second)


from datetime import date

current_date = date.today() # Fecha actual del sistema
print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.weekday())

current_date = date(1984,1,10) # Fecha definida
print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.weekday())


# Operaciones con fecha
current_date = date(current_date.year + 1, current_date.month + 1, current_date.day + 1)
print(current_date.year)
print(current_date.month)
print(current_date.day)

# Resta de dos objetos datetime del mismo tipo
diff = year_2023 - now
print(diff) # 59 days, 14:16:06.979981

# Resta a nivel de date solamente
diff = year_2023.date() - now.date()
print(diff) # 60 days, 0:00:00


# Trabajar con franjas de tiempo
from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(200, 350, 100, weeks=13)

print("***********")
print(start_timedelta)
print(end_timedelta)
print(end_timedelta - start_timedelta)