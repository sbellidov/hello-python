### Lists ###

from unicodedata import name


mi_lista = list()
mi_otra_lista = []

print(mi_lista)
print(len(mi_lista))

mi_lista = [35, 24, 62, 52, 30, 30, 17]
print(mi_lista)
print(len(mi_lista))

mi_otra_lista = [38, 1.77, 'Sergio', 'Bellido']
print(type(mi_otra_lista))
print(len(mi_otra_lista))
print(mi_otra_lista)

print(mi_otra_lista[0]) # Trae el primer elemento
print(mi_otra_lista[1]) # Trae el segundo elemento
print(mi_otra_lista[-1]) # Trae el último elemento
# Se puede contar del primero al último (empezando en cero)
# O bien contar desde el último empezando en -1
# Si se llama a un elemento que está fuera de la lista da error de ejecución:

# print(mi_otra_lista[4]) IndexError
# print(mi_otra_lista[-5]) IndexError

print(mi_otra_lista.count('Sergio')) # Resultado:1 (Retorna el número de ocurrencias de un valor)
print(mi_otra_lista.count(30)) # Resultado:0 (Retorna el número de ocurrencias de un valor)

# Desempaquetado (Ojo, si cambian el número de elementos hace que falla)
edad, altura, nombre, apellido = mi_otra_lista
print(f'edad: ', edad)
print(f'altura:', altura)
print(f'nombre:', nombre)
print(f'apellido:', apellido)
# Importatnte, necesita de todos los elementos

# Otra manera: llamando directamente al índice (Ojo, da muchos problemas)
edad, altura, nombre, apellido = mi_otra_lista[0],mi_otra_lista[1],mi_otra_lista[2],mi_otra_lista[3]
print(f'edad: ', edad)
print(f'altura:', altura)
print(f'nombre:', nombre)
print(f'apellido:', apellido)

# Operaciones con listas listas
print(mi_lista + mi_otra_lista)
print(mi_lista * 2)
# print(mi_lista * mi_otra_lista) Error
# print(mi_lista - mi_otra_lista) Error

# En Python como regla general NO existen las constantes...
# Pro convención se declararía así una variable para hacer ver que es 'constante'
# MY_CONST = 3.14

# Añadir elemento:
mi_otra_lista.append("Málaga") # Inserta al final
print(mi_otra_lista)

# Con insert puedo añadir en una posición concreta... y 'corre' la lista
mi_otra_lista.insert(1,"Rojo")
print(mi_otra_lista)

# Modificar el valor de un índice
mi_otra_lista[1] = 'Negro'
print(mi_otra_lista)
'''
# Remove (Elimina el primer elemento que le coincide, en caso de haber varios)
mi_otra_lista.remove("Rojo") # Lo elimina si lo encuentra, sino da error
print(mi_otra_lista)
'''
print(mi_lista)
mi_lista.remove(30) # Elimina el primer '30'
print(mi_lista)
mi_lista.remove(30) # Elimina el segundo '30'
print(mi_lista)
# mi_lista.remove(30) # Da error porque no encuentra ningún '30'

# Elimina el último elemento de la lista
mi_lista.pop()
print(mi_lista)

# Visualiza el elemento al que se le ha hecho pop
print(mi_lista.pop())

# Elegir el elemento que se quiere desapilar
print(mi_lista.pop())
my_pop_element = mi_lista.pop(0)
print(mi_lista)

# Restauro la lista con todos sus valores...
mi_lista = [35, 24, 62, 52, 30, 30, 17]
print(mi_lista)

# elimino el valor con 'del' --> Elimina el valor solamente, útil para el caso en que no tenga que hacer nada con él
del mi_lista[2]
print(mi_lista)

# pop vs del -->>   El 'pop' permite traer el valor del elemento eliminado para hacer algo con él.
#                   pop se suele usar de forma genérica con pop() para desapilar el último elemento

# 'del' elimina por índice
# 'remove' elimina el primer valor coincidente que encuentre

# Vaciar la lista
mi_lista.clear()
print(mi_lista)

# Copiar la lista
mi_lista = [35, 24, 62, 52, 30, 30, 17]
mi_nueva_lista = mi_lista.copy()
mi_lista.clear()
print(mi_lista)
print(mi_nueva_lista)

# Reverse
mi_nueva_lista.reverse()
print(mi_nueva_lista)

# Sort (ordenación)
mi_nueva_lista.sort() # por defecto de menor a mayor u order alfabético
print(mi_nueva_lista)

# Slice (rebanadas)
mi_lista = [35, 24, 62, 52, 30, 30, 17]
print(mi_lista[1:3])