# Exercises - Day 11

# Exercises: Level 1

# 1 - Declare a function add_two_numbers. It takes two parameters and it returns a sum.
from cmath import sqrt
from keyword import iskeyword


def add_two_numbers(num1,num2):
    return num1+num2
print(add_two_numbers(8,4)) # Test => 12

# 2 - Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def circle_area(radius):
    return 3.14 * radius ** 2
print(circle_area(14)) # Test => 615.44

# 3 - Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
#       Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums (*nums):
    total = 0
    for num in nums:
        if isinstance(num,int):
            total += num
        else:
            return 'Solo son válidos números enteros'
    return total
print(add_all_nums(8,9,7,2,1,3,-4,8,3))
print(add_all_nums(8,9,7,2,1,3,-4,'a',3))

# 4 - Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
#       Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * (9/5) ) + 32
print(f'32ºC son {convert_celsius_to_fahrenheit(32)}ºF')

# 5 - Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in ('diciembre','enero','febrero'):
        return 'Invierno'
    elif month in ('marzo','abril','mayo'):
        return 'Primavera'
    elif month in ('junio','julio','agosto'):
        return 'Verano'
    elif month in ('septiembre','octubre','noviembre'):
        return 'Otoño'
    else:
        return 'Error: Mes desconocido'
print(f'Mes: enero -> {check_season("enero".lower())}')
print(f'Mes: Marzo -> {check_season("Marzo".lower())}')
print(f'Mes: June -> {check_season("June".lower())}')
print(f'Mes: Octubre -> {check_season("Octubre".lower())}')

# 6 - Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1,x2,y1,y2):
    return (y2-y1)/(x2-x1)
print(calculate_slope(
    x1 = 2,
    y1 = 3,
    x2 = 0,
    y2 = 0
))

# 7 - Quadratic equation is calculated as follows: ax² + bx + c = 0.
#       Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c):
    x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    return [x1,x2]
print(solve_quadratic_eqn(1,3,2))
print(solve_quadratic_eqn(-1,8,0))

# 8 - Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(list):
    for element in list:
        print(element)
print_list(['Sofia','Alberto','Sergio','Laura'])

# 9 - Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
#       print(reverse_list([1, 2, 3, 4, 5]))
#       # [5, 4, 3, 2, 1]
#       print(reverse_list1(["A", "B", "C"]))
#       # ["C", "B", "A"]
def reverse_list(list):
    inverted_list = []
    for item in list:
        inverted_list.insert(0,item)
    return inverted_list

print(reverse_list([1,8,9,45,20,0,47]))
print(reverse_list(['A','r','t','v','g']))

# 10 - Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(words):
    capitalized_words = []
    for item in words:
        capitalized_words.append(item.capitalize())
    return capitalized_words

print(capitalize_list_items(['Hola', 'esto', 'es', 'una', 'prueba', 'de', 'capitalizar', 'las', 'palabras']))

# 11 - Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
#       food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
#       print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
#       numbers = [2, 3, 7, 9];
#       print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]

def add_item(list,item):
    list.append(item)
    return list

print(add_item(food_staff, 'Meat'))
print(add_item(numbers, 5))


# 12 - Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
#       food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
#       print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
#       numbers = [2, 3, 7, 9];
#       print(remove_item(numbers, 3))  # [2, 7, 9]
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]

def remove_item(list,item):
    list.remove(item)
    return list

print(remove_item(food_staff, 'Mango'))
print(remove_item(numbers, 3))


# 13 - Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
#       print(sum_of_numbers(5))  # 15
#       print(sum_all_numbers(10)) # 55
#       print(sum_all_numbers(100)) # 5050
def sum_of_numbers(number):
    total = 0
    for i in range(0,number+1):
        total += i
    return total
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

# 14 - Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def is_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False

def sum_of_odds(number):
    total = 0
    for i in range(0,number+1):
        if is_odd(i):
            total += i
    return total
print(sum_of_odds(5))
print(sum_of_odds(10))
print(sum_of_odds(100))

# 15 - Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.
def sum_of_even(number):
    total = 0
    for i in range(0,number+1):
        if not is_odd(i):
            total += i
    return total
print(sum_of_even(5))
print(sum_of_even(10))
print(sum_of_even(100))

# Exercises: Level 2
# 1 - Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
def evens_and_odds (number) :
    odds = 0
    even = 0
    for i in range(0,number+1):
        if is_odd(i):
            odds += 1
        else:
            even += 1
    return [odds,even]

print(evens_and_odds(100))


# 2 - Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(number):
    resultado = 1
    for i in range (1,number+1):
        resultado *= i
    return resultado
print(factorial(9))

# 3 - Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(*parameter):
    if len(parameter) == 0:
        return True
    else:
        return False

print(is_empty('gas'))
print(is_empty(1))
print(is_empty(True))
print(is_empty())
print(is_empty(''))
print(is_empty(False))

# 4 - Write different functions which take lists.
#       They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
values = [ 8, 5, 6, 4, 1, 3, 9, 4, 6, 5, 3, 1, 1, 8, 9, 5, 4, 3, -1, -4, 12, 3 ]

def calculate_mean (list):
    return round( sum(list) / len(list) , 2 )

def calculate_median (list):
    list.sort()
    return list[len(list)//2]

def calculate_range (list):
    return max(list) - min(list)
'''
def calculate_mode (list):
    valores_unicos = set(list)
    new_dict = dict.fromkeys(valores_unicos)
    for i in valores_unicos:
        new_dict[i] = list.count(i)
    new_dict_ordered = dict(sorted(new_dict.items(), key=lambda item: item[1]))
    lista_ordenada = new_dict_ordered.keys()
    return lista_ordenada
'''

def calculate_variance (list):
    avg = calculate_mean(values)
    numerador = []
    for item in list:
        numerador.append((item - avg)**2)
    varianza = sum(numerador) / len(list)
    return round(varianza,2)

def calculate_std (list):
    return round(sqrt(calculate_variance(list)).real, 2)


print(f'Media: {calculate_mean(values)}')
print(f'Mediana: {calculate_median(values)}')
print(f'Rango: {calculate_range(values)}')
# print(f'Moda: {calculate_mode(values)}')
print(f'Varianza: {calculate_variance(values)}')
print(f'Desv std: {calculate_std(values)}')



# Exercises: Level 3
# 1 - Write a function called is_prime, which checks if a number is prime.
def is_prime(number):
    divisores = 0
    for i in range(1,number+1):
        if number % i == 0:
            divisores += 1
    if divisores > 2:
        return False
    else:
        return True

for num in range(0,201):
    print(f'{num} es primo? {is_prime(num)}')

# 2 - Write a functions which checks if all items are unique in the list.
sample1 = [1 , 5 , 6 , 8 , 2 , 3 , 8 , 'a' , 'z' , 4]
sample2 = [1 , 5 , 6 , 8 , 2 , 3 , 8 , 'a' , True , 'z' , 4]
sample3 = [1 , 5 , 6 , 8 , 2 , 3 , 'a' , 'z' , 4]
sample4 = [1 , 5 , 6 , 8 , 2 , 3 , 4 , 4]

def all_items_are_unique(list): # Función que acepta una lista
    for element in list: # Recorro cada elemento de la lista
        list.remove(element) # Elimino el elemento de la lista ...
        if element in list: # ... y compruebo si sigue estando (lo que implicaría que hay más de uno xD )
            return False # En el momento en que me encuentre un duplicado devuelvo un False
    return True # Si no hay ningún elemento repetido devuelvo un True

print('all_items_are_unique')
print(all_items_are_unique(sample1))
print(all_items_are_unique(sample2))
print(all_items_are_unique(sample3))

# 3 - Write a function which checks if all the items of the list are of the same data type.
def all_items_same_type(list):
    types = []
    for element in list:
        types.append(type(element))
    if len(set(types)) > 1 :
        return False
    else:
        return True

print('all_items_same_type')
print(all_items_same_type(sample1))
print(all_items_same_type(sample2))
print(all_items_same_type(sample3))
print(all_items_same_type(sample4))

# 4 - Write a function which check if provided variable is a valid python variable
def is_valid_variable(variable):
    if variable.isidentifier() and not iskeyword(variable):
        return True
    else:
        return False

print('is_valid_variable')
print(is_valid_variable('a'))
print(is_valid_variable('2'))
print(is_valid_variable('def'))
print(is_valid_variable('True'))
print(is_valid_variable('true'))

# 5 - Go to the data folder and access the countries-data.py file.
#   * Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
import countries_data
def most_spoken_languages (topX):
    list = []
    for country in countries_data.countries:
        for language in country['languages']:
            list.append(language)

    most_spoken = dict.fromkeys(set(list))
    for language in most_spoken:
        most_spoken[language] = list.count(language)
    most_spoken_ordered_dict = sorted(most_spoken, key=most_spoken.get, reverse=True)
    top = 0
    while top < topX:
        print(top+1,"-",most_spoken_ordered_dict[top])
        top += 1

print(f"Los {7} idiomas hablados en más paises son: (en order descendente)")
most_spoken_languages(7)

#   * Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(topX):
    from operator import itemgetter
    countries_ordered_by_population_desc = sorted(countries_data.countries, key=itemgetter('population'), reverse=True) # Ordenación por población desc
    # https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary
    top = 0
    while top < topX:
        print(top+1,"-",countries_ordered_by_population_desc[top]['name'],":",countries_ordered_by_population_desc[top]['population'])
        top += 1

print(f"Los {18} paises más poblados son: (en order descendente)")
most_populated_countries(18)