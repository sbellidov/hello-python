# Exercises - Day 16

# 1 - Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime
print(f"Day: {datetime.now().day}")
print(f"Month: {datetime.now().month}")
print(f"Year: {datetime.now().year}")
print(f"Hour: {datetime.now().hour}")
print(f"Minute: {datetime.now().minute}")
print(f"Timestamp: {datetime.now().timestamp()}")


# 2 - Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

# 3 - Today is 5 December, 2019. Change this time string to time.
string = "5 December, 2019"
string_to_time = datetime.strptime(string,"%d %B, %Y")
print(string_to_time.date())

# 4 - Calculate the time difference between now and new year.
today = datetime.now()
new_year = datetime(year = today.year + 1, month = 1, day=1, hour=0, minute=0, second=0 )
diff = new_year - today
print(diff)

# 5 - Calculate the time difference between 1 January 1970 and now.
today = datetime.now()
jan_first_1970= datetime(year = 1970, month = 1, day=1, hour=0, minute=0, second=0 )
diff = today - jan_first_1970
print(diff)


# 6 - Think, what can you use the datetime module for? Examples:
#        - Time series analysis
#        - To get a timestamp of any activities in an application
#        - Adding posts on a blog


# Ejercicio voluntario: buble que recorre fechas aleatorias entre 1970 y 2023
# pero solo imprime en pantalla aquellas fechas que son posteriores a hoy
import random
dates = []
for i in range(1500):
    new_date = datetime(
        year = random.randrange(1970,2023),
        month = random.randrange(1,13),
        day= random.randrange(1,20)
    ).date()
    if new_date > today.date():
        print(new_date)
    dates.append(new_date.strftime("%Y-%m-%d"))
