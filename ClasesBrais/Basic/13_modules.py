### MODULES ###

# importar módulo completo
import my_module

# from 10_functions import sum_two_values (No puede empezar por número)

my_module.sumValues(5, 3, 4)
my_module.printValue("Hola Python!")


# ---------------------------
# importar funciones concretas y dejarlas disponibles
from my_module import sumValues, printValue

sumValues(4,6,8)
printValue ('Hola')


# ---------------------------
# Módulo integrado en el sistema de Python
import math

print(math.pi)
print(math.pow(2,8))


# ---------------------------
# Módulo integrado en el sistema de Python
from math import pi as num_pi

print(num_pi)