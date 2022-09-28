# Exercises - Day 10

# Exercises: Level 1
# 1 - Iterate 0 to 10 using for loop, do the same using while loop.
for num in range(11):
    print(num)
num = 0
while num <= 10:
    print(num)
    num+=1

# 2 - Iterate 10 to 0 using for loop, do the same using while loop.
for num in range(10,-1,-1):
    print(num)
num = 10
while num >= 0:
    print(num)
    num-=1

# 3 - Write a loop that makes seven calls to print(), so we get on the output the following triangle:
# 
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
for i in range(8):
    for j in range(i):
        print('#',end='')
    print('')

# 4 - Use nested loops to create the following:

# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
for i in range(8):
    for j in range(8):
        print('#',end=' ')
    else:
        print('#')

# 5 - Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
for num in range(11):
    print(f'{num} x {num} = {num*num}')

# 6 - Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in list:
    print(item)

# 7 - Use for loop to iterate from 0 to 100 and print only even numbers
for num in range (0,101,2):
    print(num)
 
# 8 - Use for loop to iterate from 0 to 100 and print only odd numbers
for num in range (1,100,2):
    print(num)

# Exercises: Level 2
# 1 - Use for loop to iterate from 0 to 100 and print the sum of all numbers.
#       The sum of all numbers is 5050.
suma = 0
for num in range(101):
    suma = suma + num
print('La suma de todos los número entre 0 y 100 es:',suma)

# 2 - Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
#       The sum of all evens is 2550. And the sum of all odds is 2500.
pares = 0
impares = 0
for num in range(101):
    if num % 2:
        impares = impares + num
    else:
        pares = pares + num
print('Los pares suman:',pares,'y los impares suman:',impares)


# Exercises: Level 3
# 1 - Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word 'land'.
from ast import Set
import countries
for pais in countries.countries:
    if 'land' in pais:
        print(pais)

# 2 - This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon', 'potato']
new_fruits = []
index = len(fruits)-1
while index >=0:
    new_fruits.append(fruits[index])
    index-=1
print(fruits)
print(new_fruits)

# 3 - Go to the data folder and use the countries_data.py file.
import countries_data

#   3.1 - What are the total number of languages in the data
list = []
for country in countries_data.countries:
    for language in country['languages']:
        list.append(language)
print(f'Hay un total de {len(set(list))} idiomas diferentes en el mundo')

#   3.2 - Find the ten most spoken languages from the data
most_spoken = dict.fromkeys(set(list))
for language in most_spoken:
    most_spoken[language] = list.count(language)
most_spoken_ordered_dict = sorted(most_spoken, key=most_spoken.get, reverse=True)
print("Los 10 idiomas hablados en más paises son: (en order descendente)")
top = 0
while top < 10:
    print(top+1,"-",most_spoken_ordered_dict[top])
    top += 1

#   3.3 - Find the 10 most populated countries in the world
from operator import itemgetter
countries_ordered_by_population_desc = sorted(countries_data.countries, key=itemgetter('population'), reverse=True) # Ordenación por población desc
# https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary

top = 0
while top <= 10:
    print(top+1,"-",countries_ordered_by_population_desc[top]['name'],":",countries_ordered_by_population_desc[top]['population'])
    top += 1
