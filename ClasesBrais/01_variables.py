# Variables

# Sería correcto pero va contra la forma de escribir Python
MyVariable = "My string variable"
print(MyVariable)

my_variable = "Mi variable !!"
print(my_variable)

my_int_variable = 82
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

print(my_int_variable, my_bool_variable , my_variable)

'''
Cambios de tipo:
str() -> To String
int() -> To Integer
'''

#Algunas funciones del sistema
print(len(my_variable))

print("Este es el valor de:" , my_bool_variable)

#Variables en una sola linea
nombre, apellido, edad = "Sergio" , "Bellido" , 38
print("Mi edad es" , edad , "y me llamo" , nombre , apellido)

# Input de datos
name = input("Dime tu nombre")
print ("Tu nombre es" , name)

# Forzado de tipos (se indica a nivel de deseo, pero no fuerza el tipo de la variable)
# Tiene más sentido en los 'input'
address:str = "Dirección"
address = 100
print (address)