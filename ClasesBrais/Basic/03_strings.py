### Strings ###

from asyncio import _set_running_loop
from sre_constants import SRE_FLAG_IGNORECASE


my_string = "Mi string"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con salto de linea"
print(my_tab_string)

my_scape_string = "\\tEste es un string\\n\tcon salto de linea"
print(my_scape_string) # Duplicar la barra \ escapa la operación


# Formateo

name, surname, age = "Sergio" , "Bellido" , 38
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # Esta forma es preferida porque
# garantiza que la variable sea del tipo que se espera: %s -> String , %d -> Integer , ...

#Así no lo deberíamos hacer:
print("Mi nombre es "+ name + " " + surname + " y mi edad es " + str(age)) #Age hay que pasarlo a String

print(f"Mi nombre es {name} {surname} y mi edad es {age}") # Muy útil y recomendada. Poniendo la 'f'


# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(d)


# División
language_slice = language[1:3]
print(language_slice) #Saca 'yt' (sin contar el 3)

language_slice = language[1:]
print(language_slice) #Saca 'ython'

language_slice = language[-2]
print(language_slice) #Saca 'o'

language_slice = language[1:2:4]
print(language_slice) #Saca 'y'

language_slice = language[0:6:2]
print(language_slice) #Saca 'Pto' Saca las posiciones alternas


# Reverse
reversed_language = language[::-1]
print(reversed_language)


# Funciones
print(language.capitalize())
print(language.upper())
print(language.count("t")) # Cuenta cuantas 't' hay
print(language.isnumeric())
print("344".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.replace("o","u"))
print(language.startswith("Py"))