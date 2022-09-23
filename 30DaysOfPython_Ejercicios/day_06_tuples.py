# Exercises - Day 6

# Exercises LEVEL 1

# 1 - Create an empty tuple
tupla = ()
print(tupla)

# 2 - Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
hermanos = ('Jose', 'Fran')
hermanas = ('Marta',) # Ojo! Añadir una coma al final del elemento para que Python lo reconozca como tupla

# 3 - Join brothers and sisters tuples and assign it to siblings
familia = hermanos + hermanas
print(familia)

# 4 - How many siblings do you have?
print(len(familia))

# 5 - Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = familia + ('Manolo',) + ('Paquita',)
print(family_members)

# Exercises LEVEL 2
# 1 - Unpack siblings and parents from family_members
hermano_mayor, hermano_mediano, hermana_ficticia, padre, madre = family_members
print(f"Hermano Mayor: {hermano_mayor}")
print(f"Hermano Mediano: {hermano_mediano}")
print(f"Hermana ficticia: {hermana_ficticia}")
print(f"Padre: {padre}")
print(f"Madre: {madre}")

# 2 - Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
frutas = ('Chirimoya', 'Mango', 'Sandía')
vegetales = ('Espárragos', 'Alcachofa', 'Calabacín')
animales = ('Tigre', 'Alpaca', 'Jirafa')
comida_tupla = frutas + vegetales + animales
print(comida_tupla)

# 3 - Change the about food_stuff_tp tuple to a food_stuff_lt list
comida_list = list(comida_tupla)
print(comida_list)

# 4 - Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(comida_tupla[len(comida_tupla)//2])

# 5 - Slice out the first three items and the last three items from food_staff_lt list
print(comida_list[0:3]) # First 3 elements
print(comida_list[-3:]) # Last 3 elements

# 6 - Delete the food_staff_tp tuple completely
del comida_tupla

# 7 - Check if an item exists in tuple:
#       - Check if 'Estonia' is a nordic country
#       - Check if 'Iceland' is a nordic country
# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(nordic_countries)
print(f"¿Estonia está en la lista? {'Estonia' in nordic_countries}")
print(f"¿Iceland está en la lista? {'Iceland' in nordic_countries}")