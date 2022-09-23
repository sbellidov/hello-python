### LOOPS ###

# While
mi_condicion = 0
while mi_condicion <= 10:
    print(mi_condicion)
    mi_condicion += 2
else:           
    print("Ya no se cumple la condición!")
print("Continúa la ejecución")
# Se le puede añadir un else que se ejecuta justo al dejar de cumplirse la condición


# Bucles con condicionales dentro
mi_condicion = 0
while mi_condicion < 20:
    mi_condicion += 1
    if mi_condicion == 15:
        print("Mi condición es 15")
    print(mi_condicion)


# Uso del BREAK para interrumpir un bucle
mi_condicion = 0
while mi_condicion < 20:
    mi_condicion += 1
    if mi_condicion == 15:
        print("Se detiene la ejecución")
        break
    print(mi_condicion)


# Bucle FOR (con listas)
mi_lista = [13, 58, 89, 42, 12, 34, 78, 12, 6]
for element in mi_lista: 
    print(element)

# Bucle FOR (con tuplas)
mi_tupla = (38, 1.77, "Sergio", "Bellido")
for element in mi_tupla: 
    print(element)

# Bucle FOR (con set)
mi_set = {'SQL', 'DAX', 'Python', 'Javascript'}
for element in mi_set:
    print(element)

# Bucle FOR (con dictionaries) 
# --- Solo imprime la CLAVE, no el VALOR
mi_dict = {'Nombre': 'Sergio', 'Apellido': 'Bellido', 'Edad': 38, 1:'Python', 0:1000000}
for element in mi_dict:
    print(element)
# --- Solo imprime el VALOR, no la CLAVE
mi_dict = {'Nombre': 'Sergio', 'Apellido': 'Bellido', 'Edad': 38, 1:'Python', 0:1000000}
for element in list(mi_dict.values()):
    print(element)


# Bucle FOR (con interrupción en función del contenido) 
mi_dict = {'Nombre': 'Sergio', 'Apellido': 'Bellido', 'Edad': 38, 1:'Python', 0:1000000}
for element in mi_dict:
    if element == 'Edad':
        break
    print(element)
else:
    print("Bucle finalizado por BREAK")
# Cuando nos salimos de un bucle con un break no tienen en cuenta el else

# El CONTINUE aborta la ejecución de ese dicle del buble y continúa con el siguiente.
# En general está desaconsejado su uso