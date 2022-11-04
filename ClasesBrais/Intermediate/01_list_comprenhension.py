### List comprenhension ###

my_original_list = [35, 24, 62, 52, 30, 30, 17]
my_list = [i for i in my_original_list]

print(my_original_list)
print(my_list) # Devuleve lo mismo


# Crea listas estableciendo un rango
my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_list = [i for i in range(8)]
print(my_list)  # [0, 1, 2, 3, 4, 5, 6, 7]

# Crear una lista con un rango
my_list = range(8)
print(list(my_list)) # [0, 1, 2, 3, 4, 5, 6, 7]

# Crear una lista con un rango alterando los valores ( multiplicado por 2 )

           ##### <- Aquí puedo poner lo que quiera
my_list = [i * i for i in range(8)]
print(my_list)  # [0, 1, 4, 9, 16, 25, 36, 49]


# Aplicándole funciones

def add_five(number):
    return number + 5

my_list = [add_five(i) for i in range(8)]
print(my_list)  # [0, 1, 4, 9, 16, 25, 36, 49]