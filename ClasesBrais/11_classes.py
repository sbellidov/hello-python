### CLASSES ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())


class Person:
    def __init__(self, name, surname): # Esto no es una función, es un constructor de clase
        self.name = name
        self.surname = surname

my_person = Person('Sergio','Bellido')
print(my_person.name)
print(f'{my_person.name} {my_person.surname}')


class Person2:
    def __init__(self, name, surname): # Esto no es una función, es un constructor de clase
        self.full_name = f'{name} {surname}'

my_person = Person2('Sergio','Bellido')
print(my_person.full_name)

# Me permite definir funciones
class Person3:
    def __init__(self, name, surname): # Esto no es una función, es un constructor de clase
        self.full_name = f'{name} {surname}'
    
    def caminar (self):
        print(f'{self.full_name} está caminando')

my_person = Person3('Sergio','Bellido')
print(my_person.full_name)
my_person.caminar()


# Me permite definir funciones
class Person4:
    def __init__(self, name, surname, alias = 'Sin alias'): # Esto no es una función, es un constructor de clase
        self.full_name = f'{name} {surname} ({alias})'
    
    def caminar (self):
        print(f'{self.full_name} está caminando')

my_person = Person4('Sergio','Bellido')
print(my_person.full_name)
my_person.caminar()

my_other_person = Person4('Laura', 'Guirado' , 'Plinky')
print(my_other_person.full_name)
my_other_person.caminar()

# El constructor de clases es mutable
my_other_person.full_name = "Maritrini Lija (La Cabra)"
print(my_other_person.full_name)


# Variable privada con __ (doble guión antes del nombre)
class Person5:
    def __init__(self, name, surname, alias = 'Sin alias'): # Esto no es una función, es un constructor de clase
        self.full_name = f'{name} {surname} ({alias})'
        self.__name = name
        self.__surname = surname
    
    def get_name(self):
        return self.__name
    
    def caminar (self):
        print(f'{self.full_name} está caminando')

persona = Person5('Sergio', 'Bellido')
persona.__name = 'Hola'
print(persona.get_name())
