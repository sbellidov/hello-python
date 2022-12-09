# Exercises - Day 19

# Exercises: Level 1

# 1 - Write a function which count number of lines and number of words in a text.
# All the files are in the data the folder:

def print_number_of_lines (filename, person_name):
    with open('30DaysOfPython_Ejercicios/data_files/'+filename,'r') as file:
        print(f"{person_name}: Lines => {len(file.readlines())}")

def print_number_of_words (filename, person_name):
    with open('30DaysOfPython_Ejercicios/data_files/'+filename,'r') as file:
        print(f"{person_name}: Words => {len(file.read().strip().split(' '))}")

# a) Read obama_speech.txt file and count number of lines and words
print_number_of_lines('obama_speech.txt', 'Obama')
print_number_of_words('obama_speech.txt', 'Obama')

# b) Read michelle_obama_speech.txt file and count number of lines and words
print_number_of_lines('michelle_obama_speech.txt', 'Michelle')
print_number_of_words('michelle_obama_speech.txt', 'Michelle')

# c) Read donald_speech.txt file and count number of lines and words
print_number_of_lines('donald_speech.txt', 'Donald')
print_number_of_words('donald_speech.txt', 'Donald')

# d) Read melina_trump_speech.txt file and count number of lines and words
print_number_of_lines('melania_trump_speech.txt', 'Melania')
print_number_of_words('melania_trump_speech.txt', 'Melania')
# 
# 2 - Read the countries_data.json data file in data directory,
# create a function that finds the ten most spoken languages

#       # Your output should look like this
#       print(most_spoken_languages(filename='./data/countries_data.json', 10))
#       [(91, 'English'),
#       (45, 'French'),
#       (25, 'Arabic'),
#       (24, 'Spanish'),
#       (9, 'Russian'),
#       (9, 'Portuguese'),
#       (8, 'Dutch'),
#       (7, 'German'),
#       (5, 'Chinese'),
#       (4, 'Swahili'),
#       (4, 'Serbian')]
#       
#       # Your output should look like this
#       print(most_spoken_languages(filename='./data/countries_data.json', 3))
#       [(91, 'English'),
#       (45, 'French'),
#       (25, 'Arabic')]

import json

def most_spoken_languages(filename, top):
    countries_file = open(filename,'r')
    countries_dict = json.load(countries_file)


    list_of_all_languages = [] # Mando todos los elementos de 'languages' a una lista
    for i in range(len(countries_dict)):
        list_of_all_languages += countries_dict[i]['languages']

    most_spoken = { x:list_of_all_languages.count(x) for x in list_of_all_languages } # Creo un diccionario con el idioma como key y número de repeticiones como value
    most_spoken_sorted = list(sorted(most_spoken.items(), key=lambda item: item[1] , reverse=True)) # Diccionario ordenado descendente por valor
    most_spoken_sorted_formatted = []
    for i in most_spoken_sorted:
        most_spoken_sorted_formatted.append((i[1],i[0]))
    print(f'*** {top} Most spoken languages ***')
    for i in range(0,top):
        print(most_spoken_sorted_formatted[i])
    countries_file.close()

most_spoken_languages('30DaysOfPython_Ejercicios/data_files/countries_data.json',10)
most_spoken_languages('30DaysOfPython_Ejercicios/data_files/countries_data.json',3)


# 3 - Read the countries_data.json data file in data directory,
# create a function that creates a list of the ten most populated countries

#       # Your output should look like this
#       print(most_populated_countries(filename='./data/countries_data.json', 10))
#       
#       [
#       {'country': 'China', 'population': 1377422166},
#       {'country': 'India', 'population': 1295210000},
#       {'country': 'United States of America', 'population': 323947000},
#       {'country': 'Indonesia', 'population': 258705000},
#       {'country': 'Brazil', 'population': 206135893},
#       {'country': 'Pakistan', 'population': 194125062},
#       {'country': 'Nigeria', 'population': 186988000},
#       {'country': 'Bangladesh', 'population': 161006790},
#       {'country': 'Russian Federation', 'population': 146599183},
#       {'country': 'Japan', 'population': 126960000}
#       ]
#       
#       # Your output should look like this
#       
#       print(most_populated_countries(filename='./data/countries_data.json', 3))
#       [
#       {'country': 'China', 'population': 1377422166},
#       {'country': 'India', 'population': 1295210000},
#       {'country': 'United States of America', 'population': 323947000}
#       ]
def most_populated_countries(filename, top):
    file = open(filename,'r')
    file_json = json.load(file)

    sorted_list = sorted(file_json, key=lambda d: d['population'], reverse=True)[0:top]
    sorted_list_formatted = []
    for i in sorted_list:
        sorted_list_formatted.append({'country': i['name'],'population': i['population']})
    print(f'*** {top} Most populated countries ***')
    print(*sorted_list_formatted,sep='\n')
    file.close()

most_populated_countries('30DaysOfPython_Ejercicios/data_files/countries_data.json',10)
most_populated_countries('30DaysOfPython_Ejercicios/data_files/countries_data.json',4)


# Exercises: Level 2

# 4 - Extract all incoming email addresses as a list from the email_exchange_big.txt file.
import re
emails_file = open('30DaysOfPython_Ejercicios/data_files/email_exchanges_big.txt','r').read()

regex_email_pattern = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
emails_found = re.findall(regex_email_pattern, emails_file)

print(len(list(set(emails_found))))


# 5 - Find the most common words in the English language. Call the name of your function find_most_common_words,
# it will take two parameters - a string or a file and a positive integer, indicating the number of words.

# Your function will return an array of tuples in descending order. Check the output
#       # Your output should look like this
#       print(find_most_common_words('sample.txt', 10))
#       [(10, 'the'),
#       (8, 'be'),
#       (6, 'to'),
#       (6, 'of'),
#       (5, 'and'),
#       (4, 'a'),
#       (4, 'in'),
#       (3, 'that'),
#       (2, 'have'),
#       (2, 'I')]
#   
#       # Your output should look like this
#       print(find_most_common_words('sample.txt', 5))
#   
#       [(10, 'the'),
#       (8, 'be'),
#       (6, 'to'),
#       (6, 'of'),
#       (5, 'and')]

def clean_text (text):
    import string
    text = text.lower() # Normalizado a minúsculas
    text = text.translate({ord(c): None for c in string.punctuation+'¡'}) # Eliminados signos de puntuación
    text = text.replace('\n',' ') # Cambio retornos de carro por espacios
    text = text.split()
    return text

def count_words (words):
    return list(map(lambda x:(x,words.count(x)), list(set(words))))

def sort_words (words):
    return sorted(words, key=lambda x: x[1], reverse=True)

def find_most_common_words(filename,filetop):
    with open(filename, 'r') as file:
        return sort_words(count_words(clean_text(file.read())))[:filetop]

print(find_most_common_words('30DaysOfPython_Ejercicios/data_files/sample_text_1.txt',10))
print(find_most_common_words('30DaysOfPython_Ejercicios/data_files/sample_text_2.txt',10))


# 6 - Use the function, find_most_frequent_words to find:
#   a) The ten most frequent words used in Obama's speech
print(f'*** Obama speach - Palabras más repetidas ***')
print(find_most_common_words('30DaysOfPython_Ejercicios/data_files/obama_speech.txt',10))

#   b) The ten most frequent words used in Michelle's speech
print(f'*** Michelle Obama speach - Palabras más repetidas ***')
print(find_most_common_words('30DaysOfPython_Ejercicios/data_files/michelle_obama_speech.txt',10))

#   c) The ten most frequent words used in Trump's speech
print(f'*** Donald Trump speach - Palabras más repetidas ***')
print(find_most_common_words('30DaysOfPython_Ejercicios/data_files/donald_speech.txt',10))

#   d) The ten most frequent words used in Melina's speech
print(f'*** Melania Trump speach - Palabras más repetidas ***')
print(find_most_common_words('30DaysOfPython_Ejercicios/data_files/melania_trump_speech.txt',10))


# 7 - Write a python application that checks similarity between two texts.
#    [X] It takes a file or a string as a parameter and it will evaluate the similarity of the two texts.
#    [X] For instance check the similarity between the transcripts of Michelle's and Melina's speech.
#    [ ] You may need a couple of functions:
#        [X] function to clean the text(clean_text)
#        [X] function to remove support words(remove_support_words) List of stop words are in the data directory
#    [ ] and finally to check the similarity(check_text_similarity).
from data_files.stop_words import stop_words

def get_content(file_txt):
    try:
        file = open(file_txt).read()
        return file
    except FileNotFoundError:
        return file_txt

def clean_text_2(text):
    text = text.lower() # Normalizado a minúsculas
    text = text.replace('\n',' ') # Cambio retornos de carro por espacios
    text = text.replace('.',' ') # Cambio puntos por espacios
    text = text.replace(',',' ') # Cambio comas por espacios
    text = text.replace('—',' ') # Cambio guiones por espacios
    text = text.split()
    return text

def filter_words_in_list( words_list , filter_list ):
    return list(filter(lambda word: word not in filter_list , words_list))

def check_similarity(file_txt_1,file_txt_2):
    file_1 = get_content(file_txt_1)
    file_2 = get_content(file_txt_2)

    file_1 = clean_text_2(file_1)
    file_2 = clean_text_2(file_2)

    file_1 = filter_words_in_list(file_1, stop_words)
    file_2 = filter_words_in_list(file_2, stop_words)

    import difflib
    result = difflib.SequenceMatcher(a = file_1, b = file_2)
    return result.ratio()

print(check_similarity(
    '30DaysOfPython_Ejercicios/data_files/michelle_obama_speech.txt',
    '30DaysOfPython_Ejercicios/data_files/melania_trump_speech.txt'
    ))
# Result: 0.06405

print(check_similarity('Sergio es muy guapo','Muy guapo es Alberto'))
# Result: 0.5


# 8 - Find the 10 most repeated words in the romeo_and_juliet.txt
print(f'*** Palabras más repetidas en Romeo y Julieta ***')
print(find_most_common_words('30DaysOfPython_Ejercicios/data_files/romeo_and_juliet.txt',10))

# 9 - Read the hacker news csv file and find out:
#   a) Count the number of lines containing python or Python
#   b) Count the number lines containing JavaScript, javascript or Javascript
#   c) Count the number lines containing Java and not JavaScript


import csv
# Resolución usando csv
with open('30DaysOfPython_Ejercicios/data_files/hacker_news.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count_contain_python = 0
    line_count_contain_javascript = 0
    line_count_contain_java = 0
    for row in csv_reader:
        for element in row:
            if 'python' in element.lower():
                line_count_contain_python += 1
                break
            if 'javascript' in element.lower():
                line_count_contain_javascript += 1
                break
            elif 'java' in element.lower():
                line_count_contain_java += 1
                break
print(f'Number of lines with Python: {line_count_contain_python}')
print(f'Number of lines with Javascript: {line_count_contain_javascript}')
print(f'Number of lines with Java: {line_count_contain_java}')
#   Number of lines with Python: 179
#   Number of lines with Javascript: 181
#   Number of lines with Java: 64

# Resolución usando txt
with open('30DaysOfPython_Ejercicios/data_files/hacker_news.csv') as file_txt:
    file = file_txt.read().splitlines()
    for line in file:
        if 'python' in line.lower():
            line_count_contain_python += 1
            break
        if 'javascript' in line.lower():
            line_count_contain_javascript += 1
            break
        elif 'java' in line.lower():
            line_count_contain_java += 1
            break
print(f'Number of lines with Python: {line_count_contain_python}')
print(f'Number of lines with Javascript: {line_count_contain_javascript}')
print(f'Number of lines with Java: {line_count_contain_java}')
#   Number of lines with Python: 179
#   Number of lines with Javascript: 182
#   Number of lines with Java: 64
