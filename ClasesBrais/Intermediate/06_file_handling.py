### File Handling ###
import os

# .txt file
txt_file = open('ClasesBrais/Intermediate/my_file.txt', 'w+') # 'r' para Lectura y 'w' para Escritura
# r+ ==> Leer y escribir

txt_file.write('Mi nombre es Sergio Bellido\nSoy Ingeniero analista de datos\nTengo 38 años')

#print(txt_file.read())
#print(txt_file.read(10)) # Lee solo los 10 primeros caracteres
#print(txt_file.readline()) # Mi nombre es Sergio Bellido
#print(txt_file.readline()) # Soy Ingeniero de análisis de datos
#print(txt_file.readlines()) # ['Mi nombre es Sergio Bellido\n', 'Soy Ingeniero de análisis de datos\n', 'Tengo 38 años y estoy aprendiendo Python']

txt_file.write("\nMe gusta el triatlón")
print(txt_file.readlines())
'''
# Elimina un fichero
os.remove('ClasesBrais/Intermediate/my_file.txt')
'''

# .json file
import json

json_file = open('ClasesBrais/Intermediate/my_file.json', 'w+')
json_text = {
    'name': 'Sergio',
    'surname': 'Bellido',
    'age': 38,
    'gender': 'Hombre',
    'country': 'Spain',
    'city': 'Málaga',
    'languages': ['Python', 'SQL', 'JavaScript']
}
#json_file.write(json_file) ===>> TypeError: write() argument must be str, not _io.TextIOWrapper

json.dump(json_text, json_file, indent = 4) # El 'dump' es específico para grabar los json

json_file.close() # Cerramos la escritura para después abrirlo en lectura

with open('ClasesBrais/Intermediate/my_file.json') as json_file:
    for line in json_file.readlines():
        print(line)

json_dict = json.load(open('ClasesBrais/Intermediate/my_file.json'))
print(json_dict)
print(type(json_dict))
print(json_dict['name'])

# .csv file
import csv
# Lectura
csv_file = open('ClasesBrais/Intermediate/my_file.csv','w+')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'surname', 'age', 'language', 'website'])
csv_writer.writerow(['Sergio', 'Bellido', '38', 'Python', 'None'])
csv_writer.writerow(['Roswell', '', 2, 'Python', 'None'])
csv_file.close()

with open('ClasesBrais/Intermediate/my_file.csv') as my_csv_file:
    for line in my_csv_file:
        print(line)

# .xlsx file
# import xlrd # Debe instalarse el módulo

# .xml file
import xml