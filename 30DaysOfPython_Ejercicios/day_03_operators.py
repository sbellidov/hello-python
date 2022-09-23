# Exercises - Day 3

# 1 - Declare your age as integer variable
edad = 38

# 2 - Declare your height as a float variable
altura = 1.77

# 3 - Declare a variable that store a complex number
complejo = 5 + 3j

# 4 - Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
print("*** Área del triángulo ***")
base = float(input("Base del triángulo: "))
altura = float(input("Altura del triángulo: "))
print(f"El área del triángulo es { base * altura * 0.5 }")

# 5 - Write a script that prompts the user to enter side a, side b, and side c of the triangle.
# Calculate the perimeter of the triangle (perimeter = a + b + c).
print("*** Perímetro del triángulo ***")
lado_a = float(input("Longitud del primer lado: "))
lado_b = float(input("Longitud del segundo lado: "))
lado_c = float(input("Longitud del tercer lado: "))
print(f"El perímetro del triángulo es: { lado_a + lado_b + lado_c }")

# 6 - Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
print("*** Rectángulo: Área y Perímetro ***")
lado_a = float(input("Longitud del lado largo: "))
lado_b = float(input("Longitud del lado corto: "))
print(f"El área del rectángulo es: { lado_a * lado_b }")
print(f"El perímetro del rectángulo es: { 2 * (lado_a + lado_b) }")

# 7 - Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
print("*** Círculo: Área y Perímetro ***")
r = float(input("Radio del círculo: "))
print(f"El área del círculo es: { pi * r * r }")
print(f"La circunferencia es: { 2 * pi * r }")

# 8 - Calculate the slope, x-intercept and y-intercept of y = 2x -2
print("*** Pendiente y cortes con X e Y de y=2x-2 ***")
x_intercept_value_x = 0
x_intercept_value_y = -2
y_intercept_value_x = -1
y_intercept_value_y = 0
print(f"Corte con el eje X en: ({x_intercept_value_x},{x_intercept_value_y})")
print(f"Corte con el eje Y en: ({y_intercept_value_x},{y_intercept_value_y})")
pendiente_8 = (y_intercept_value_y-x_intercept_value_y)/(y_intercept_value_x-x_intercept_value_x)
print(f"Pendiente: {pendiente_8}")

# 9 - Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math
print("*** Pendiente y distancie euclidea de (2,2) y (6,10) ***")
x1,y1 = 2,2
x2,y2 = 6,10
print(f"Pendiente: {(y2-y1)/(x2-x1)}")
pendiente_9 = round(math.sqrt((y2-y1)**2 + (x2-x1)**2),2)
print(f"Distancia euclidiana: { pendiente_9 }")

# 10 - Compare the slopes in tasks 8 and 9.
print("*** Comparar pendientes de los ejercicios 8 y 9 ***")
print(f"Ejercicio 8. Pendiente: {pendiente_8}")
print(f"Ejercicio 9. Pendiente: {pendiente_9}")

# 11 - Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
print("*** Ecuación y = x^2 + 6x + 9 ***")
x = int(input("Introduce el valor de X: "))
print(f"Resultado { x**2 + 6*x + 9 }") # Valor de x=-3 hace la y=0

# 12 - Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(f"Longitud de Python: { len('Python')}")
print(f"Longitud de Dragon: { len('Dragon')}")
print(f"Falsy comparison (String): {'Python'=='Dragon'}")
print(f"Falsy comparison (Lenght): {len('Python')==len('Dragon')}")

# 13 - Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# 14 - I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon"
print('jargon' in sentence)

# 15 - There is no 'on' in both dragon and python
print('on' not in 'python' and 'on' not in 'dragon')

# 16 - Find the length of the text python and convert the value to float and convert it to string
print(str(float(len("Python"))))

# 17 - Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
print("*** Comprobador de números pares ***")
numero = int(input("Introduzca un número entero: "))
print(f"¿El número {numero} es par? => {numero%2 == 0}")

# 18 - Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7//3==int(2.7))
print(f"7//3 = {7//3}")
print(f"int(2.7) = {int(2.7)}")

# 19 - Check if type of '10' is equal to type of 10
print(type('10')==type(10))

# 20 - Check if int('9.8') is equal to 10
print(int(float('9.8'))==10) #Se obtiene un error, hay que convertir primero a float y luego a int

# 21 - Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
print("*** Calculadora de salarios ***")
horas = float(input("Introduzca número de horas trabajadas: "))
tarifa = float(input("Introduzca la tarifa (€/h): "))
print(f"Importe a pagar: {round((horas*tarifa),2):.2f}€") # Añadir el ' :.2f ' hace que rellene con ceros el decimal

# 22 - Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live.
#      Assume a person can live hundred years
print("*** Calculadora de tiempo de vida en segundos ***")
years = int(input("Introduzca los años vividos: "))
print(f"Segundos vividos: {years * 365 * 24 * 60 * 60}")

# 23 - Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
var = 1
print(f"{var} {var**0} {var**1} {var**2} {var**3}")
var = 2
print(f"{var} {var**0} {var**1} {var**2} {var**3}")
var = 3
print(f"{var} {var**0} {var**1} {var**2} {var**3}")
var = 4
print(f"{var} {var**0} {var**1} {var**2} {var**3}")
var = 5
print(f"{var} {var**0} {var**1} {var**2} {var**3}")