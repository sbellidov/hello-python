# Exercises - Day 14

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercises: Level 1

# 1 - Explain the difference between map, filter, and reduce.
_map = "Acepta un iterable junto a una función. Devuelve el iterable al que se le ha aplicado la función a cada elemento"
_filter = "Acepta un iterable junto a una función que debe devolver un boolenano. Devuelve solo aquellos valores del iterable que son True"
_reduce = "Acepta un iterable junto a una función con 2 parámetros. Devuelve un solo valor (no otro iterable. Empieza con el 1º y 2º, el primer resultado junto con el 3º es el siguiente"

# 2 - Explain the difference between higher order function, closure and decorator
_higher_order_function = "Función que devuelve una función"
_closure = "Funciones anidadas. El valor mandado a una función se trasvasa a la subyacente"
_decorator = "Asigna una función a una variable y ya ésta puede ser usada como la propia función"

# 3 - Define a call function before map, filter or reduce, see examples.
# 4 - Use for loop to print each country in the countries list.
for item in countries:
    print(item)

# 5 - Use for to print each name in the names list.
for item in names:
    print(item)

# 6 - Use for to print each number in the numbers list.
for item in numbers:
    print(item)


# Exercises: Level 2

# 1 - Use map to create a new list by changing each country to uppercase in the countries list
print(list(map(lambda country: country.upper() ,countries)))

# 2 - Use map to create a new list by changing each number to its square in the numbers list
print(list(map(lambda number: number**2 ,numbers)))

# 3 - Use map to change each name to uppercase in the names list
print(list(map(lambda name: name.upper() ,names)))

# 4 - Use filter to filter out countries containing 'land'.
print(list(filter(lambda text: 'land' in text , countries)))

# 5 - Use filter to filter out countries having exactly six characters.
print(list(filter(lambda text: len(text) == 6 , countries)))

# 6 - Use filter to filter out countries containing six letters and more in the country list.
print(list(filter(lambda text: len(text) >= 6 , countries)))

# 7 - Use filter to filter out countries starting with an 'E'
print(list(filter(lambda text: text[0] == 'E' , countries)))

# 8 - Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
print(list(filter( lambda item: len(item) > 6 ,list(map(lambda item: item.upper(),countries )))))

# 9 - Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
input_list = ['Hola', 89, True, [7,'X'], 'string', 'Se acaba', 7, False]

def get_string_lists(lista):
    return list(filter( lambda item : type(item) == str , lista))

print(get_string_lists(input_list))

# 10 - Use reduce to sum all the numbers in the numbers list.
from functools import reduce
print(reduce(lambda x,y: x+y , numbers, 0))

# 11 - Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def join_countries(first_word, second_word):
    if second_word:
        return first_word + ", " + second_word
    else:
        return "b"

print(reduce(join_countries,countries) + " are north European countries")

# 12 - Declare a function called categorize_countries that returns a list of countries with some common pattern
# (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
import countries

def categorize_countries(countries_list, pattern):
    print(list(filter(lambda text: pattern.lower() in text.lower() , countries_list)))

#pattern_input = input('Introduzca patrón de búsqueda de paises: ')
#categorize_countries(countries.countries, pattern_input)

# 13 - Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def create_dict_using_first_letter(country_list):
    country_list_first_letter = list(map(lambda item: item[0] , country_list ))
    return { x:country_list_first_letter.count(x) for x in country_list_first_letter }
    
print(create_dict_using_first_letter(countries.countries))


# 14 - Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.py list in the data folder.
def get_first_ten_countries(country_list):
    x = 10
    return country_list[:x]

print(get_first_ten_countries(countries.countries))

# 15 - Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(country_list):
    x = 10
    return country_list[-x:len(country_list)]

print(get_last_ten_countries(countries.countries))

# Exercises: Level 3

# 1 - Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
#   * Sort countries by name, by capital, by population
import countries_data

def print_sorted(countries, sorting, limit='', reverse=False):
    sorted_list = sorted(countries, key=lambda d: d[sorting] , reverse=reverse )
    for i in range(limit or len(sorted_list)):
        print(i+1,"-",sorted_list[i]['name'],"(",sorted_list[i]['population'],")","-",sorted_list[i]['capital'])

print_sorted(countries_data.countries,'population')
print_sorted(countries_data.countries,'name')
print_sorted(countries_data.countries,'capital')

#   * Sort out the ten most spoken languages by location.

list_of_all_languages = [] # Mando todos los elementos de 'languages' a una lista
for i in range(len(countries_data.countries)):
    list_of_all_languages += countries_data.countries[i]['languages']

most_spoken = { x:list_of_all_languages.count(x) for x in list_of_all_languages } # Creo un diccionario con el idioma como key y número de repeticiones como value
most_spoken_sorted = dict(sorted(most_spoken.items(), key=lambda item: item[1] , reverse=True)) # Diccionario ordenado descendente por valor

from itertools import islice    # Me quedo con los top 10 de lenguajes más hablados
def take(top, most_spoken_sorted):
    return list(islice(most_spoken_sorted, top))

print(take(10,most_spoken_sorted))

'''
country_list_first_letter = list(map(lambda item: item[0] , country_list ))
    return { x:country_list_first_letter.count(x) for x in country_list_first_letter }
'''



#   * Sort out the ten most populated countries.
print_sorted(countries_data.countries,'population',10,True)

'''
   {
        "name": "American Samoa",
        "capital": "Pago Pago",
        "languages": [
            "English",
            "Samoan"
        ],
        "population": 57100,
        "flag": "https://restcountries.eu/data/asm.svg",
        "currency": "United State Dollar"
    },
'''