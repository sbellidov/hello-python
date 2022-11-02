### DICTIONARIES ###
# Clave valor

mi_dict = dict()
mi_otro_dict = {}

print(type(mi_dict))
print(type(mi_otro_dict))

mi_dict = {
    'Nombre': 'Sergio',
    'Apellido': 'Bellido',
    'Edad': 38,
    1:'Python',
    0:1000000
}

mi_otro_dict = {
    'Nombre': 'Sergio',
    'Apellido': 'Bellido',
    'Edad': 38,
    'Lenguajes':{'Python','Javascript','Node.js'}
}

print(mi_dict)
print(mi_otro_dict)

print(len(mi_dict))
print(len(mi_otro_dict))

print(mi_dict['Nombre']) # 'Sergio'

mi_dict['Nombre'] = 'Laura'
print(mi_dict)

print(mi_dict[0]) # 1000000 # Ojo, poner la key en int o string según sea

# Añadir elementos
mi_dict['Estudios Universitarios'] = True
print(mi_dict)

# Elimina un elemento de un diccionario
del mi_dict[0]
print(mi_dict)

# Búsquedas
print('Sergio' in mi_dict) # False
print('Sergio' in mi_dict['Nombre']) # False
print('Nombre' in mi_dict) # True

# Funciones
print(mi_dict.items()) # Diccionario completo: dict_items([('Nombre', 'Laura'), ('Apellido', 'Bellido'), ('Edad', 38), (1, 'Python'), ('Estudios Universitarios', True)])
print(mi_dict.keys()) # Lista de claves: dict_keys(['Nombre', 'Apellido', 'Edad', 1, 'Estudios Universitarios'])
print(mi_dict.values()) # Lista de valores: dict_values(['Laura', 'Bellido', 38, 'Python', True])

mi_nuevo_dict = dict.fromkeys(("Nombre",1)) # Crea un nuevo diccionario sin valores
print(mi_nuevo_dict)

mi_nuevo_dict = dict.fromkeys(mi_dict) # Crea un nuevo diccionario sin valores, lo crea con todas las claves de mi_dict
print(mi_nuevo_dict)

mi_nuevo_dict = dict.fromkeys(mi_dict,("Prueba1","Prueba2")) # inserta el valor (o valores) que le pasemos
print(mi_nuevo_dict)

print(list(mi_nuevo_dict))
print(tuple(mi_nuevo_dict))
print(set(mi_nuevo_dict))

# Para mostrar los valores
print(list(mi_dict.values()))