# Echar un vistazo a: https://fastapi.tiangolo.com/es/python-types/

# Una variable declarada...
my_variable = "My string variable"
print(my_variable)
print(type(my_variable))

# ... puede cambiar de tipo
my_variable = 5
print(my_variable)
print(type(my_variable))

# Se puede declarar el tipo de variable (le ayuda al editor y ayuda a FastAPI a detectar errores de tipo)
my_typed_variable: str = "My typed String variable"
print(my_typed_variable)
print(type(my_typed_variable))

# ... no obstante al ser Python un lenguaje de 'tipado débil' pueda cambiar el tipo sin generar error
my_typed_variable = 5
print(my_typed_variable)
print(type(my_typed_variable))
