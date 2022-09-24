# Exercises - Day 8

# 1 - Create an empty dictionary called dog
dog = {}
print(type(dog))

# 2 - Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name': 'Tango',
    'color': 'Blanco',
    'breed': 'Carlino',
    'legs': 'Cortas',
    'age': 5
}
print(dog)

# 3 - Create a student dictionary and add:
#       first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Sergio',
    'last_name': 'Bellido',
    'gender': 'Hombre',
    'marital_status': 'Divorciado',
    'skills': ['Data & Analytics','Python','SQL'],
    'country': 'Spain',
    'city': 'Málaga',
}
print(student)

# 4 - Get the length of the student dictionary
print(len(student))

# 5 - Get the value of skills and check the data type, it should be a list
print('Skills: ',student['skills'])

# 6 - Modify the skills values by adding one or two skills
student['skills'].append('PowerBI')
student['skills'].append('Electronic')
print('Skills: ',student['skills'])

# 7 - Get the dictionary keys as a list
print(list(student.keys()))

# 8 - Get the dictionary values as a list
print(list(student.values()))

# 9 - Change the dictionary to a list of tuples using items() method
print(student.items())

# 10 - Delete one of the items in the dictionary
student.pop('city')
print(student)

# 11 - Delete one of the dictionaries
del dog