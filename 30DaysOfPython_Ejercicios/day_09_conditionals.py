# Exercises - Day 9

# Exercises: Level 1

# 1 - Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive.
# If below 18 give feedback to wait for the missing amount of years. Output:
#       Enter your age: 30
#       You are old enough to learn to drive.
#       Output:
#       Enter your age: 15
#       You need 3 more years to learn to drive.
edad = int(input('Introduce la edad: '))
if edad >= 18:
    print('You are old enough to drive')
else:
    print(f'Tienes que esperar {18-edad} años para poder conducir')

# 2 - Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
# Output:
#       Enter your age: 30
#       You are 5 years older than me.
mi_edad = 38
tu_edad = int(input('Introduce tu edad: '))
if tu_edad == mi_edad:
    print('Somos de la misma edad !')
elif tu_edad > mi_edad:
    if tu_edad - mi_edad == 1:
        print('Eres un año mayor que yo')
    else:
        print(f'Eres {tu_edad - mi_edad} años mayor que yo')
else:
    if mi_edad - tu_edad == 1:
        print('Eres un año menor que yo')
    else:
        print(f'Eres {mi_edad - tu_edad} años menor que yo')

# 3 - Get two numbers from the user using input prompt. If a is greater than b return a is greater than b,
# if a is less b return a is smaller than b, else a is equal to b. Output:
#       Enter number one: 4
#       Enter number two: 3
#       4 is greater than 3
a = int(input('Introduce primer número: '))
b = int(input('Introduce segundo número: '))
if a > b :
    print(a,'es mayor que',b)
elif a < b:
    print(a,'es menor que',b)
else:
    print(a,'es igual a',b)

# Exercises: Level 2
# 1 - Write a code which gives grade to students according to theirs scores:
# 
#       90-100, A
#       70-89, B
#       60-69, C
#       50-59, D
#       0-49, F
score = int(input('Introduce el score del estudiante (0 ~ 100): '))
if score >= 90:
    print('Grade A')
elif score >= 70:
    print('Grade B')
elif score >= 60:
    print('Grade C')
elif score >= 50:
    print('Grade D')
else:
    print('Grade F')

# 2 - Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn.
# December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
mes = input('Introduce el mes: ').capitalize()
if mes in ('Diciembre','Enero', 'Febrero'):
    print('Invierno')
elif mes in ('Marzo','Abril', 'Mayo'):
    print('Primavera')
elif mes in ('Junio','Julio', 'Agosto'):
    print('Verano')
elif mes in ('Septiembre','Octubre', 'Noviembre'):
    print('Otoño')
else:
    print("Error: nombre del mes no encontrado")

# 3 - The following list contains some fruits:
#       fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
# If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input('Añade una fruta: ').lower()
if new_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(new_fruit)
    print(fruits)


# Exercises: Level 3
# 4 - Here we have a person dictionary. Feel free to modify it!
# 
#         person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }
persona = {
    'first_name': 'Sergio',
    'last_name': 'Bellido',
    'age': 38,
    'country': 'Spain',
    'is_marred': False,
    'skills': ['JavaScript', 'PowerBI', 'SQL', 'Python', 'Project Management', 'React'],
    'address': {
        'street': 'Sierra de Ronda',
        'number': 1,
        'zipcode': '29720'
        }
    }

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if persona.get('skills'):
    print(persona['skills'][len(persona['skills'])//2])
else:
        print('No existe skills !!')

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if persona.get('skills'):
    if 'Python' in persona['skills']:
        print('SI, tiene skills de Python')
    else:
        print('No tiene conocimientos de Python')
else:
    print('No tiene skills')

#  * If a person skills has only JavaScript and React, print('He is a front end developer'),
#       if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
#       if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),
#       else print('unknown title') - for more accurate results more conditions can be nested!
if 'React' and 'Node' and 'MongoDB' in persona['skills']:
    print('He is a fullstack developer')
elif 'Node' and 'Python' and 'MongoDB' in persona['skills']:
    print('He is a backend developer')
elif 'JavaScript' and 'React' in persona['skills']:
    print('He is a frontend developer')
else:
    print('unknown title')
    
#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.
if persona['is_marred'] and persona['country']=='Finland':
    print(persona['first_name'],persona['last_name'],'lives in Finland. He is married')