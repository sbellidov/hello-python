### Tuples ###
# La principal diferencia respecto a las listas es que es inmutable una vez declarada
# No permite modificar, añadir o borrar valores

# Definición de una tupla
mi_tupla = tuple() # con su palabra reservada
mi_otra_tupla = ()

mi_tupla = (38, 1.77, "Sergio", "Bellido")
print(mi_tupla)
print(type(mi_tupla))

# Puedo acceder a valores determinados mostrando 
print(mi_tupla[0])
print(mi_tupla[-1])
#print(mi_tupla[4]) IndexError
#print(mi_tupla[-6]) IndexError

print(mi_tupla.count("Sergio")) # Cuenta elementos que coinciden (igual que en listas)

print(mi_tupla.index(38))

# mi_tupla[1] = 1.80 # TypeError: 'tuple' object does not support item assignment

mi_otra_tupla = (38, 60, 30, 90) # Si la tupla está vacía puedo añadirle valores
print(mi_tupla + mi_otra_tupla) # Puedo sumar dos tuplas

tupla_suma = mi_tupla + mi_otra_tupla # también podría asignarla para crear una nueva tupla
print(tupla_suma)

# Slices
print(tupla_suma[3:6]) # Desde el índice 3 al 6 (sin tener en cuenta el 6)

# Convertir una tupla en lista (para hacerla mutable)
print(type(mi_tupla))
mi_tupla = list(mi_tupla)
print(type(mi_tupla))

# Ahora puedo aprovechar de añadir valores a la tupla convertida en lista
mi_tupla.append('Malaga')
mi_tupla = tuple(mi_tupla)
print(mi_tupla)
print(type(mi_tupla))

# A pesar de que las tuplas son inmutables, permite borrar la tupla con 'del'
# del mi_tupla[0]  # No permite eliminar un elemento de la tupla
print(mi_tupla)

del mi_tupla
# print(mi_tupla)