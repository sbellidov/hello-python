### Operadores ###

print ( 3 + 4 ) # Suma
print ( 3 - 4 ) # Resta
print ( 3 * 4 ) # Producto
print ( 3 / 4 ) # División
print ( 10 % 3 ) # Módulo
print ( 10 // 3 ) # Floor división (División entera)
print ( 10 ** 3 ) # Exponente

print ( 2 ** 3 + 2 - 7 / 1 // 4 ) # Combinación de operadores

print ("Hola" + "Python") # Concatena !
# print ("Hola" - "Python") # No todos los operadores funcionan
# print ("Hola" + 5) # No Funciona
print ("Hola" + str(5)) # Funciona

print ( "Hola " * 10 ) # Saca la palabra 'Hola' 10 veces. Tiene que ser número entero


### Operadores Comparativos ###

print ( 3 > 4 )
print ( 3 < 4 )
print ( 3 <= 4 )
print ( 3 >= 4 )
print ( 3 == 4 )
print ( 3 != 4 )

# Considera la ordenación alfabétca. Tiene en cuenta las mayúsculas y minúsculas
print ( "Hola" > "Python" )
print ( "Hola" < "Python" )
print ( "Hola" <= "Python" )
print ( "Hola" >= "Python" )
print ( "Hola" == "Python" )
print ( "Hola" != "Python" )


### Operadores lógicos ###

print ( 3 > 4 and "Hola" > "Python") # &&
print ( 3 > 4 or  "Hola" > "Python") # ||
#print ( 3 > 4 not "Hola" > "Python") # !=
print ( not(3 > 4) )