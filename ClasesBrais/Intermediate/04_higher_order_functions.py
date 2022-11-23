### Higher Order Functions ###

def sum_one(value):
    return value + 1

# def sum_two_values(first_value, second_value):
#     return first_value + second_value + 1

def sum_two_values(first_value, second_value):
    return sum_one(first_value + second_value)

print(sum_two_values(5,6))

#------ En funciones de órden superior se puede pasar una función como parámetro

def sum_two(value):
    return value + 2

def sum_four(value):
    return value + 4

def two_values_and_something(value1, value2, function):
    return function(value1 + value2)

print(two_values_and_something(5,5,sum_two)) # 12
print(two_values_and_something(5,5,sum_four)) # 14



### Closures ###

def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()
print(add_closure(9))



### Built-in Higher Order Functions ###

numbers = [2, 5, 10, 21, 3, 30]

# --- Map ---
def multiply_two(number):
    return number * 2

# Itera una lista a la que le aplica la función que le pasemos
print(list(map(multiply_two, numbers))) # [4, 10, 20, 42]

# Aquí cobraría más sentido trabajar con lambdas
print(list(map(lambda number: number * 2, numbers))) # [4, 10, 20, 42]


# --- Filter ---
def filter_greater_than_ten(num):
    if num > 10:
        return True
    return False

print(filter(filter_greater_than_ten,numbers)) # Genera un objeto: <filter object at 0x000002C4431F3CD0>
print(list(filter(filter_greater_than_ten,numbers))) # [21, 30]

print(list(filter(lambda number:number > 10 ,numbers))) # [21, 30]


# --- Reduce ---
from functools import reduce

def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values, numbers))