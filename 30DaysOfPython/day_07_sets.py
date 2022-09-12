# Exercises - Day 7
'''
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1
# 1 - Find the length of the set it_companies
print(len(it_companies))

# 2 - Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3 - Insert multiple IT companies at once to the set it_companies
it_companies.update({'Salesforce','TikTok','Youtube'})
print(it_companies)

# 4 - Remove one of the companies from the set it_companies
it_companies.remove('IBM')
print(it_companies)

# 5 - What is the difference between remove and discard
it_companies.discard('IBM') # Si el valor a eliminar no existe no hace nada. Es idempotente
print(it_companies)
#it_companies.remove('IBM') KeyError: 'IBM' # Remove da error si no encuentra el valor a eliminar


# Exercises: Level 2
# 1 - Join A and B
print('\n***Join A and B***')
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(f'A: {A}')
print(f'B: {B}')
A.update(B)
print(A)

# 2 - Find A intersection B
print('\n***Find A intersection B***')
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(f'A: {A}')
print(f'B: {B}')
A.intersection(B)
print(A)

# 3 - Is A subset of B
print('\n***Is A subset of B***')
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(f'A: {A}')
print(f'B: {B}')
print(A.issubset(B)) # True

# 4 - Are A and B disjoint sets
print('\n***Are A and B disjoint sets***')
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(f'A: {A}')
print(f'B: {B}')
print(A.isdisjoint(B)) # False

# 5 - Join A with B and B with A
print('\n***Join A with B and B with A***')
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(f'A: {A}')
print(f'B: {B}')
A.update(B)
B.update(A)
print(A)
print(B)

# 6 - What is the symmetric difference between A and B
print('\n***What is the symmetric difference between A and B**')
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(f'A: {A}')
print(f'B: {B}')
print(A.symmetric_difference(B))

# 7 - Delete the sets completely
del A,B
'''
# Exercises: Level 3
age_list = [22, 19, 24, 25, 26, 24, 25, 24]
# 1 - Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age_list)
print(age_list,age_set)
print(f"Lista: {len(age_list)}")
print(f"Set: {len(age_set)}")

# 2 - Explain the difference between the following data types: string, list, tuple and set
print('STRING: Concatenación de caracteres que forman una o más palabras. Puede trabajarse cada letra como si de un elemento de una lista se tratara')
print('LISTA: Un conjunto de elementos que pueden estar repetidos y con un orden establecido. Su contenido es modificable')
print('TUPLA: Un conjunto de elementos que pueden estar repetidos y con un orden establecido. Su contenido es ininmutable una vez declarada')
print('LIST: Conjunto de valores, no repetidos, sin orden establecido, modificable')

# 3 - I am a teacher and I love to inspire and teach people.
# How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
print(f'Palabras únicas usadas: {len(set(sentence.split()))}')