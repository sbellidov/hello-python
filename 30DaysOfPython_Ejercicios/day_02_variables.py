# Exercises - Day 2

# Write a python comment saying 'Day 2: 30 Days of python programming'

# LEVEL 1

# Declare a first name variable and assign a value to it
first_name = 'Sergio'

# Declare a last name variable and assign a value to it
last_name = 'Bellido'

# Declare a full name variable and assign a value to it
full_name = first_name + ' ' + last_name

# Declare a country variable and assign a value to it
country = 'Spain'

# Declare a city variable and assign a value to it
city = 'Malaga'

# Declare an age variable and assign a value to it
age = 38

# Declare a year variable and assign a value to it
year = 1984

# Declare a variable is_married and assign a value to it
# Declare a variable is_true and assign a value to it
# Declare a variable is_light_on and assign a value to it
# Declare multiple variable on one line
is_married , is_true, is_light_on = False, True, False




# LEVEL 2

# 1 - Check the data type of all your variables using type() built-in function
print(first_name, "is type:" , type(first_name))
print(last_name, "is type:" , type(last_name))
print(full_name, "is type:" , type(full_name))
print(country, "is type:" , type(country))
print(city, "is type:" , type(city))
print(age, "is type:" , type(age))
print(year, "is type:" , type(year))
print(is_married, "is type:" , type(is_married))
print(is_true, "is type:" , type(is_true))
print(is_light_on, "is type:" , type(is_light_on))

# 2 - Using the len() built-in function, find the length of your first name
print("El first_name:", first_name, "tiene una longitud de" , len(first_name) , "caracteres")

# 3 - Compare the length of your first name and your last name
print("El first_name:", first_name, "tiene una longitud de" , len(first_name) , "caracteres")
print("El last_name:", last_name, "tiene una longitud de" , len(last_name) , "caracteres")

# 4 - Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# I - Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print("Total:" , total)

# II - Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print("Diff:" , diff)

# III - Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print("Product:" , product)

# IV - Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print("Division:" , division)

# V - Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print("Remainder:" , remainder)

# VI - Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print("Exp:" , exp)

# VI - Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print("Floor Division:" , floor_division)



# 5 - The radius of a circle is 30 meters
import math
r = 30
print("Radio:" , r , "m")

# I - Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = round(math.pi * r ** 2 , 2)
print("Area:", area_of_circle , "m2")

# II - Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = round( 2 * math.pi * r , 2)
print("Circunferencia:", circum_of_circle , "m")

# II - Take radius as user input and calculate the area
r = input("Introduce valor del radio en metros:")
print("Area:", round(math.pi * int(r) ** 2 , 2) , "m2")



# 6 - Use the built-in input function to get first name, last name,
#     country and age from a user and store the value to their corresponding variable names
first_name = input("First Name: ")
last_name = input("Last Name: ")
country = input("Country: ")
age = input("Age: ")
print("Your name is:", first_name, last_name , "from", country , "and age", age , "years old.")



# 7 - Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')

# >>> help('keywords')
# 
# Here is a list of the Python keywords.  Enter any keyword to get more help.
# 
# False               class               from                or
# None                continue            global              pass
# True                def                 if                  raise
# and                 del                 import              return
# as                  elif                in                  try
# assert              else                is                  while
# async               except              lambda              with
# await               finally             nonlocal            yield
# break               for                 not