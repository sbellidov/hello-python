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
# 9 - Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
# 10 - Use reduce to sum all the numbers in the numbers list.
# 11 - Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
# 12 - Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
# 13 - Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
# 14 - Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# 15 - Declare a get_last_ten_countries function that returns the last ten countries in the countries list.


# Exercises: Level 3

# 1 - Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
#   * Sort countries by name, by capital, by population
#   * Sort out the ten most spoken languages by location.
#   * Sort out the ten most populated countries.