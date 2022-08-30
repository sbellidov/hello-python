# Write a python comment saying 'Day 2: 30 Days of python programming'

# # LEVEL 2

# 2.1 - Comprobar la versión
# -->> Version 3.10.6

# 2.2 - Operaciones (Operadores: 3 y 4)

print( 3 + 4 ) #suma
print( 3 - 4 ) #resta
print( 3 * 4 ) #multiplicación
print( 3 % 4 ) #módulo
print( 3 / 4 ) #división
print( 3 ** 4 ) #potencia
print( 3 // 4 ) #división entera

# 2.3 - Escribir cadenas
print("Nombre: Sergio Bellido")
print("España")
print("I am enjoying 30 days of python")

# 2.4 - Comprobar tipos de datos
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("Nombre: Sergio Bellido"))
print(type("España"))


# LEVEL 3
# 3.1 - Ejemplos de tipos de datos:  Number(Integer, Float, Complex), 
# String, Boolean, List, Tuple, Set and Dictionary
print( 3 , type(3) , "Integer")
print( 3.14 , type(3.14) , "Float")
print( 5+2j , type(5+2j) , "Complex")
print( "hola" , type("hola") , "Cadena")
print( True , type(True) , "Boolean")
print( [1,2,3] , type([1,2,3]) , "Lista (Array)")
print( ("Sergio","Sofia","Alberto") , type(("Sergio","Sofia","Alberto")) , "Tupla")
print( {"Malaga","Madrid","Barcelona", 4} , type({"Malaga","Madrid","Barcelona", 4}) , "Set")
print( 
    {
        'nombre': 'Sergio',
        'apellido': 'Bellido',
        'edad': 38
    }
    , type(
        {
        'nombre': 'Sergio',
        'apellido': 'Bellido',
        'edad': 38
        })
    , "Diccionario")


# 3.2 - Find an Euclidian distance between (2, 3) and (10, 8)
# Formula: d(p,q) = sqrt( (q1-p1)*2 + (q2-p2)*2 )

p1 = 2
p2 = 3
q1 = 10
q2 = 8

import math 
distance = math.sqrt( (q1-p1)**2 + (q2-p2)**2 )
print("Distancia Euclidea entre (",p1,",",p2,") y (",q1,",",q2,") es: ", round(distance,2))