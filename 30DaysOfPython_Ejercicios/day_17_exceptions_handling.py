# Exercises - Day 17

# Exercises: Level 1

# names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia'].
# Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

try:
    nordic_countries = names[0:5]
    es = names[5]
    ru = names[6]
    print(nordic_countries)
    print(es)
    print(ru)
except Exception as error:
    print(error)
    print('*** ERROR ***')
else:
    print('La ejecución es exitosa')