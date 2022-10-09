### FUNCTIONS ###

def my_function():
    print('Esto es una función')

my_function()
my_function()
my_function()

def sum_two_numbers(first_number,second_number):
    print(first_number + second_number)

sum_two_numbers(7,6)
sum_two_numbers(895,154)
sum_two_numbers("5","89") # Cadenas de texto se concatenan


def sum_two_numbers(first_number: int,second_number: int): # especificar el tipo no sirve de nada
    print(first_number + second_number)
sum_two_numbers("5","89")
# Aunque se le fije el tipo de parámetro no va a hacer caso


# Con retorno
def sum_two_numbers_with_return(first_value,second_value):
    return(first_value + second_value)

print(sum_two_numbers_with_return(7,8))


def print_name ( name , surname ):
    print(f"{name} {surname}")
print_name( surname = 'Bellido' , name = 'Sergio' )


def print_name_with_default ( name , surname , alias = ''):
    print(f"{name} {surname} {alias}")
print_name_with_default('Sergio' , 'Bellido')
print_name_with_default('Sergio' , 'Bellido', 'Plusky')

# Envío de múltiples parámetros
def print_texts(*text):
    print(text)
print_texts('Hola','mi nombre es','Sergio')

def print_texts(*texts):
    for text in texts:
        print(text.upper())
print_texts('Hola','mi nombre es','Sergio')
