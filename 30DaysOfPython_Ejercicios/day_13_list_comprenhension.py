# Exercises - Day 13

# 1 - Filter only negative and zero in the list using list comprehension
#        numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
only_negatives = [i for i in numbers if i <= 0]
print(only_negatives)


# 2 - Flatten the following list of lists of lists to a one dimensional list :
#        list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
#    output:
#    [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten = [number for row in list_of_lists for number in row]
flatten_2 = [number for row in flatten for number in row]
print(list_of_lists)
print(flatten)
print(flatten_2)


# 3 - Using list comprehension create the following list of tuples:
# 
#       [(0, 1, 0, 0, 0, 0, 0),
#       (1, 1, 1, 1, 1, 1, 1),
#       (2, 1, 2, 4, 8, 16, 32),
#       (3, 1, 3, 9, 27, 81, 243),
#       (4, 1, 4, 16, 64, 256, 1024),
#       (5, 1, 5, 25, 125, 625, 3125),
#       (6, 1, 6, 36, 216, 1296, 7776),
#       (7, 1, 7, 49, 343, 2401, 16807),
#       (8, 1, 8, 64, 512, 4096, 32768),
#       (9, 1, 9, 81, 729, 6561, 59049),
#       (10, 1, 10, 100, 1000, 10000, 100000)]

print("********** Ejercicio 3 **********")
creation = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(creation)


# 4 - Flatten the following list to a new list:
#       countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#   output:
#   [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

countries = [('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]
def flatten(l):
    return [item for sublist in l for item in sublist]
flat = flatten(countries)
result = [(i[0].upper(), i[0].upper()[0:3], i[1].upper() ) for i in flat]
print(countries)
print(flat)
print(result)


# 5 - Change the following list to a list of dictionaries:
#       countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#       output:
#       [{'country': 'FINLAND', 'city': 'HELSINKI'},
#       {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#       {'country': 'NORWAY', 'city': 'OSLO'}]

countries = [('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]
def flatten(l):
    return [item for sublist in l for item in sublist]
flat = flatten(countries)
result = [{ 'country': i[0].upper(), 'city': i[1].upper() } for i in flat]
print(countries)
print(flat)
print(result)


# 6 - Change the following list of lists to a list of concatenated strings:
#       names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#       output
#       ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
def flatten(l):
    return [item for sublist in l for item in sublist]
flat = flatten(names)
result = [i[0] + " " + i[1] for i in flat]
print(countries)
print(flat)
print(result)


# 7 - Write a lambda function which can solve a slope or y-intercept of linear functions.

point_a_x = 5
point_a_y = 4
point_b_x = 1
point_b_y = -2

# Formula => y2-y1 / x2-x1
slope = lambda x1, y1, x2, y2 : (y2 -y1) / (x2 -x1)
print(slope(point_a_x, point_a_y, point_b_x, point_b_y))

# Formula => y = m*x +b
y_intercept = point_a_y - slope(point_a_x, point_a_y, point_b_x, point_b_y) * point_a_x
print(y_intercept)