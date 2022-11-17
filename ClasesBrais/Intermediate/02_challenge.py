### Challenges ###

'''
EL FAMOSO "FIZZ BUZZ”
 Escribe un programa que muestre por consola (con un print) los
 números de 1 a 100 (ambos incluidos y con un salto de línea entre
 cada impresión), sustituyendo los siguientes:
 - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
 - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

def fizzbuzz():
    for index in range(1, 101):
        if index % 5 == 0 and index % 3 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)

fizzbuzz()


'''
¿ES UN ANAGRAMA?
 Escribe una función que reciba dos palabras (String) y retorne
 verdadero o falso (Bool) según sean o no anagramas.
 - Un Anagrama consiste en formar una palabra reordenando TODAS
   las letras de otra palabra inicial.
 - NO hace falta comprobar que ambas palabras existan.
 - Dos palabras exactamente iguales no son anagrama.
'''

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    elif sorted(word_one.lower()) == sorted(word_two.lower()):
        return True
    return False
    

print(is_anagram("amor","roma")) # True
print(is_anagram("amor","truco")) # False
print(is_anagram("palo","palo")) # False


'''
LA SUCESIÓN DE FIBONACCI
 Escribe un programa que imprima los 50 primeros números de la sucesión
 de Fibonacci empezando en 0.
 - La serie Fibonacci se compone por una sucesión de números en
   la que el siguiente siempre es la suma de los dos anteriores.
   0, 1, 1, 2, 3, 5, 8, 13...
'''

def fibonacci():

    prev = 0
    next = 1

    for index in range(0,50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib

fibonacci()


'''
¿ES UN NÚMERO PRIMO?
 Escribe un programa que se encargue de comprobar si un número es o no primo.
 Hecho esto, imprime los números primos entre 1 y 100.
'''

def is_prime(number):
    if number < 2:
        return False
    for index in range (2,number):
        if number % index == 0:
            return False
    return True
    

for check in range(0,101):
    print(f"{check} => {is_prime(check)}")

for check in range(0,101):
    if is_prime(check):
        print(check)


'''
INVIRTIENDO CADENAS
 Crea un programa que invierta el orden de una cadena de texto
 sin usar funciones propias del lenguaje que lo hagan de forma automática.
 - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
'''

def reverse_string(text):
    reversed_text = ""
    for index in range(0,len(text)):
        reversed_text += text[len(text) - index - 1]
    return reversed_text

print(reverse_string("Hola mundo"))