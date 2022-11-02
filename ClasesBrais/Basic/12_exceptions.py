### EXCEPTIONS HANDLING ###

numberOne = 5
numberTwo = 1
numberTwo = '1'

#print(numberOne + numberTwo) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# try except
try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except:
    #Se ejecuta cuando en el bloque del TRY se produce un error
    print('Se ha producido un error')


# try except else
try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except:
    #Se ejecuta cuando en el bloque del TRY se produce un error
    print('Se ha producido un error')
else:
    # Se ejecuta cuando NO se produce un error
    print('La ejecución continúa correctamente')


# try except else finally
try:
    print(numberOne + numberTwo)
    print('No se ha producido un error') # Si hay un error, no llega a ejecutarse, salta al except inmediatamente
except:
    #Se ejecuta cuando en el bloque del TRY se produce un error
    print('Se ha producido un error')
else:
    # Se ejecuta cuando NO se produce un error
    print('La ejecución continúa correctamente')
finally:
    # Se ejecuta siempre, pase lo que pase
    print('La ejecución continúa !!! ')


# Captura de excepciones por tipo
try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except TypeError:
    #Se ejecuta ## SOLO ## cuando en el bloque del TRY se produce un error del tipo TypeError
    print('Se ha producido un TypeError')


# Captura de excepciones por tipo (varios tipos)
try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except ValueError:
    #Se ejecuta ## SOLO ## cuando en el bloque del TRY se produce un error del tipo ValueError
    print('Se ha producido un ValueError')
except TypeError:
    #Se ejecuta ## SOLO ## cuando en el bloque del TRY se produce un error del tipo TypeError
    print('Se ha producido un TypeError')


# Captura de la información de la excepción
try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except ValueError as error:
    print(error)
except Exception as error: # Equivalente a 'except: ' pero con la ventaje de poder capturar el error. Captura cualquier tipo de error
    print(error)