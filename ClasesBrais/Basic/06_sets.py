### SETS ###
# - No admite repetidos
# - No tiene orden en sus elementos
# - Es más eficiente que otras estructuras como listas o tuplas

mi_set = set()
print(type(mi_set))

mi_otro_set = {}
print(type(mi_otro_set)) # Inicialmente es un diccionario

# Tanto SET como DICTIONARY se definen igual, con {}

mi_otro_set = {'Sergio', 'Bellido', 38}
print(type(mi_otro_set)) # Al tener datos ya el lenguaje reconoce que es un SET

print(len(mi_otro_set)) # Longitud: 3

#print(mi_otro_set[0]) # TypeError: 'set' object is not subscriptable

mi_otro_set.add('serbel')
print(mi_otro_set) # Un set no es una estructura ordenada. Lo ordena internamente con un hash
# Diferentes print sacará el set en diferente orden los elementos

# Un set no admite repetidos !!

# Forma de realizar búsquedas
print('Sergio' in mi_otro_set)
print('Hola' in mi_otro_set)

# Eliminar elementos
mi_otro_set.remove('serbel')
print(mi_otro_set)

# Clear: Vacía el contenido del set
mi_otro_set.clear()
print(len(mi_otro_set))
print(type(mi_otro_set))

del mi_otro_set
# print(mi_otro_set) NameError: name 'mi_otro_set' is not defined

# Se puede transformar en lista pero lo hará de manera diferente en cada ejecución
mi_set = {'Sergio', 'Bellido', 38}
mi_lista = list(mi_set)
print(mi_lista)

mi_otro_set = {'SQL', 'DAX', 'Python', 'Javascript'}
mi_nuevo_set = mi_set.union(mi_otro_set)
print(mi_nuevo_set)

# Union
mi_otro_set = mi_otro_set.union(mi_otro_set).union(mi_otro_set) # Recuerda: No admite duplicados
print(mi_otro_set)

mi_otro_set = mi_otro_set.union({'Swift','Pascal'}) # Puedo añadir 
print(mi_otro_set)

print(mi_nuevo_set.difference(mi_set)) # Muestras las diferencias entre dos sets... algo así como una resta
