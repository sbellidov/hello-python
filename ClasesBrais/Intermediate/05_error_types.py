### Error Types ###

# --- SyntaxError
#print 'Hola Comunidad' # SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print("Hola Comunidad!")

# --- NameError
#print(language) # NameError: name 'number' is not defined
language = 'spanish'
print(language)

# --- IndexError
my_list = ['Python', 'Swift', 'Kotlin', 'Dart', 'Javascript']
print(my_list[0])  # Python
print(my_list[-1]) # Javascript
#print(my_list[5])  # IndexError: list index out of range

# --- ModuleNotFoundError
#import maths # ModuleNotFoundError: No module named 'maths'
import math
print(math.pi)

# --- AttributeError
#print(math.PI) # AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?

# --- KeyError
my_dict = {'Nombre': 'Sergio', 'Apellido': 'Bellido', 'skills':['Data Analyst', 'SQL', 'Python'], 'edad':35 }
print(my_dict['edad'])
#print(my_dict['apelido']) # KeyError: 'apelido'
print(my_dict['Apellido'])

# --- TypeError
#print(my_list['Nombre']) # TypeError: list indices must be integers or slices, not str
print(my_list[0])

# --- ImportError
#from math import pii # ImportError: cannot import name 'pii' from 'math' (/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/lib-dynload/math.cpython-310-darwin.so)
from math import pi
print(pi)

# --- ValueError
my_int = '10'
#my_int = '10 años' # ValueError: invalid literal for int() with base 10: '10 años'
print(int(my_int))
print(type(int(my_int)))

# --- ZeroDivisionError
print(4/2)
#print(4/0) # ZeroDivisionError: division by zero