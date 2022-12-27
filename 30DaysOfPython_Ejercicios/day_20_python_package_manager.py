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
import requests
url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url).json()

import pandas as pd

df = pd.DataFrame.from_dict(response)
df = pd.concat([df, df['weight'].apply(pd.Series)], axis=1)

# Crea dataframe nuevo, separa por el símbolo ' - ' , pasa str a numeric, calcula media entre max y min y lo añade el dataset principal
weight = pd.DataFrame.from_records(df['metric'].str.split(" - "),columns=['min','max'])
weight['min'] = pd.to_numeric(weight['min'])
weight['max'] = pd.to_numeric(weight['max'])
df = pd.concat([df,weight.mean(axis='columns').apply(pd.Series).rename(columns={0:'avg_weight'})],axis=1)

# Crea dataframe nuevo, separa por el símbolo ' - ' , pasa str a numeric, calcula media entre max y min y lo añade el dataset principal
life_span = pd.DataFrame.from_records(df['life_span'].str.split(" - "),columns=['min','max'])
life_span['min'] = pd.to_numeric(life_span['min'])
life_span['max'] = pd.to_numeric(life_span['max'])
df = pd.concat([df,life_span.mean(axis='columns').apply(pd.Series).rename(columns={0:'avg_life_span'})],axis=1)

print(df[['country_code','origin','name','avg_weight','avg_life_span']])

print('\n *** Cats weight ***')
print('Weight (min):' , df['avg_weight'].min(), 'Kg')
print('Weight (max):' , df['avg_weight'].max(), 'Kg')
print('Weight (mean):' , round(df['avg_weight'].mean(),2), 'Kg')
print('Weight (median):' , round(df['avg_weight'].median(),2), 'Kg')
print('Weight (std):' , round(df['avg_weight'].std(),2), 'Kg')

print('\n *** Cats life span ***')
print('Life span (min):' , df['avg_life_span'].min(), 'years')
print('Life span (max):' , df['avg_life_span'].max(), 'years')
print('Life span (mean):' , round(df['avg_life_span'].mean(),2), 'years')
print('Life span (median):' , round(df['avg_life_span'].median(),2), 'years')
print('Life span (std):' , round(df['avg_life_span'].std(),2), 'years')

print(
    '\n *** Cats Origin frequency table ***\n',
    df.groupby('origin')['name']
    .count()
    .reset_index()
    .rename(columns={'name':'Total', 'origin':'Origin'})
    .sort_values('Origin', ascending=True)
)


# 3 - Read the countries API and find
#   a - the 10 largest countries
#   b - the 10 most spoken languages
#   c - the total number of languages in the countries API

url = 'https://restcountries.com/v2/all'
response = requests.get(url).json()
df = pd.DataFrame.from_dict(response)
print(df)


# Top 10 most populated
df.sort_values(by=['population'],inplace=True, ascending=False)
print('\n*** 10 Most populated ***')
print(df[['name','population']].head(10).rename(columns={'name':'Country','population':'Population'}))

# Top 10 largest
df.sort_values(by=['area'],inplace=True, ascending=False)
print('\n*** 10 Largest ***')
print(df[['name','area']].head(10).rename(columns={'name':'Country','area':'Area'}))

# Top 10 most spoken languages
languages = pd.json_normalize(df['languages'].explode())
print(
    '\n *** 10 Most spoken languages ***\n',
    languages.groupby('name')['nativeName']
    .count()
    .reset_index()
    .rename(columns={'name':'Language', 'nativeName':'Countries'})
    .sort_values('Countries', ascending=False)
    .head(10)
)

# Number of languages included
print('\n*** Total of languages spoken ***')
print(len(pd.unique(languages['name'])))


# 4 - UCI is one of the most common places to get data sets for data science and machine learning.
# Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php).
# Without additional libraries it will be difficult, so you may try it with BeautifulSoup4


### NO ESTÁ COMPLETO ###

import bs4 as bs
import requests
url = 'https://archive.ics.uci.edu/ml/datasets.php'

source = requests.get(url).text
soup = bs.BeautifulSoup(source,'html.parser')

tables = soup.find_all('table', {'cellpadding':'3'})

table = tables[0] # the result is a list, we are taking out data from it

for td in table.find('tr').find_all('td'):
    print(td.text)
