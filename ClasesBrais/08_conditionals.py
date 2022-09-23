### CONDITIONALS ###

from sqlite3 import enable_callback_tracebacks


mi_condicion = True
if mi_condicion:
    print("Se ejecuta la condición del IF")
print("La ejecución continúa")
# "Se ejecuta la condición del IF"
# "La ejecución continúa"

mi_condicion = False
if mi_condicion:
    print("Se ejecuta la condición del IF")
print("La ejecución continúa")
# "La ejecución continúa"

# SI se ejecuta
mi_condicion = 5*2
if mi_condicion:
    print("Se ejecuta la condición del IF")
print("La ejecución continúa")
# "Se ejecuta la condición del IF"
# "La ejecución continúa"


# NO se ejecuta
mi_condicion = 5*2
if mi_condicion == 11:
    print("Se ejecuta la condición del IF")
print("La ejecución continúa")
# "La ejecución continúa"


# SI se ejecuta
mi_condicion = 5*2
if mi_condicion >= 10:
    print("Se ejecuta la condición del IF")
print("La ejecución continúa")
# "Se ejecuta la condición del IF"
# "La ejecución continúa"


mi_condicion = 5*2
if mi_condicion > 10:
    print("Se ejecuta la condición del IF")
else:    
    print("Se ejecuta la condición del ELSE")
print("La ejecución continúa")


mi_condicion = 5*3
if mi_condicion > 10 and mi_condicion < 20:
    print("Es mayor que 10 y menor que 20")
else:    
    print("Es menor o igual que 10 o mayor o igual que 20")
print("La ejecución continúa")


mi_condicion = 9
if mi_condicion == 0:
    print("Es igual a 0")
elif mi_condicion == 1:
    print("Es igual a 1")
elif mi_condicion == 2:
    print("Es igual a 2")
else:    
    print("No es 0, 1 o 2")


mi_string = "" # Cadena vacía no entra 
if mi_string:
    print("Ha entrado")
else:
    print("No ha entrado")

mi_string = "Texto" # Cadena no vacía si entra 
if mi_string:
    print("Ha entrado")
else:
    print("No ha entrado")

mi_string = ""
if not mi_string:
    print("Cadena vacía con NOT si que entra")