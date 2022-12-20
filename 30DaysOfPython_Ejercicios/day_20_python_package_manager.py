# Exercises - Day 20

# 1 - Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
import requests
url = 'http://www.gutenberg.org/files/1112/1112.txt'
# ----------- Complementario para el aprendizaje -----------
response = requests.get(url)
print(response) # <Response [200]>
print(response.status_code) # 200
print(response.headers) #
# {
#     'Date': 'Tue, 20 Dec 2022 19:38:24 GMT',
#     'Server': 'Apache',
#     'Last-Modified': 'Sat, 17 Oct 2020 15:05:23 GMT',
#     'Accept-Ranges': 'bytes',
#     'Content-Length': '179410',
#     'Content-Type': 'text/plain'
# }
print(response.text)
# ----------- Complementario para el aprendizaje -----------

# ----------- Funciones traidas del day_19_files handling -----------
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

def find_most_common_words(text,filetop):
    return sort_words(count_words(clean_text(text)))[:filetop]
# ----------- Funciones traidas del day_19_files handling -----------

print(f'*** Palabras más repetidas en Romeo y Julieta ***')
print(find_most_common_words(response.text,10))
# Result: [('the', 866), ('and', 793), ('to', 625), ('i', 585), ('of', 535), ('a', 527), ('in', 377), ('is', 375), ('that', 363), ('you', 362)]


# 2 - Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
#   a - the min, max, mean, median, standard deviation of cats' weight in metric units.
#   b - the min, max, mean, median, standard deviation of cats' lifespan in years.
#   c - Create a frequency table of country and breed of cats
url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
cats_api = response.json()

import pandas as pd
df = pd.read_json(url, orient='records')
print(df.to_string())


# 3 - Read the countries API and find
#   a - the 10 largest countries
#   b - the 10 most spoken languages
#   c - the total number of languages in the countries API


# 4 - UCI is one of the most common places to get data sets for data science and machine learning.
# Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php).
# Without additional libraries it will be difficult, so you may try it with BeautifulSoup4

