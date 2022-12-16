### Regular Expressions ###
# https://regex101.com

import re

my_string = 'Esta es la lección número 7: Expresiones regulares'
my_other_string = 'Esta no es la lección número 6: Manejor de ficheros'

# Héctor de León => Buenas clases para aprender expresiones regulares

# Match
print('\n*** Match ***')
print(re.match('Esta es la lección', my_string)) # => <re.Match object; span=(0, 18), match='Esta es la lección'>
print(re.match('Esta es la lección', my_other_string)) # => None
print(re.match('Expresiones regulares', my_string)) # => None
# --> Match solo empieza a buscar en el principio de la cadena

# Flags
#    ASCII = A = sre_compile.SRE_FLAG_ASCII # assume ascii "locale"
#    IGNORECASE = I = sre_compile.SRE_FLAG_IGNORECASE # ignore case
#    LOCALE = L = sre_compile.SRE_FLAG_LOCALE # assume current 8-bit locale
#    UNICODE = U = sre_compile.SRE_FLAG_UNICODE # assume unicode "locale"
#    MULTILINE = M = sre_compile.SRE_FLAG_MULTILINE # make anchors look for newline
#    DOTALL = S = sre_compile.SRE_FLAG_DOTALL # make dot match newline
#    VERBOSE = X = sre_compile.SRE_FLAG_VERBOSE # ignore whitespace and comments
#    # sre extensions (experimental, don't rely on these)
#    TEMPLATE = T = sre_compile.SRE_FLAG_TEMPLATE # disable backtracking
#    DEBUG = sre_compile.SRE_FLAG_DEBUG # dump pattern after compilation
match = re.match('Esta es la lección', my_string, re.I)
if match is not None:
    print(match)
    start,end = match.span()
    print(my_string[start:end])

match = re.match('Esta es la lección', my_other_string, re.I)
if match is not None:
    print(match)
    start,end = match.span()
    print(my_other_string[start:end])


# Search
print('\n*** Search ***')
search = re.search('Esta es la lección', my_string, re.I)
print(search)
start,end = search.span()
print(my_string[start:end])


# Findall
print('\n*** Findall ***')
findall = re.findall('lección', my_string, re.I) # I => Ignora mayúsculas y minúsculas
print(findall) # <== Listado con tantas veces como lo hya encontrado. Resultado: ['lección']


# Split
print('\n*** Split ***')
print(re.split(':',  my_string)) # ['Esta es la lección número 7', ' Expresiones regulares']
print(re.split('\n', my_string)) # ['Esta es la lección número 7: Expresiones regulares']


# Sub
print('\n*** Sub ***')
print(re.sub('Expresiones', 'expresiones', my_string))
print(re.sub('lección', 'LECCIÓN', my_string))
print(re.sub('Expresiones Regulares', 'RegEx', my_string))
# Con múltiples coincidencias:
print(re.sub('lección|Lección', 'LECCIÓN', my_string))
print(re.sub('[l|L]ección', 'LECCIÓN', my_string))


# --------- Patrones de RegEx ---------
pattern = r'[lL]ección' # con y sin mayúscula
print(re.findall(pattern, my_string)) # ['lección']

pattern = r'[lL]ección|Expresiones' # con y sin mayúscula + Expresiones
print(re.findall(pattern, my_string)) # ['lección', 'Expresiones']

pattern = r'[a-z]' # todas las letras que sean minúsculas
print(re.findall(pattern, my_string)) # ['s', 't', 'a', 'e', 's', 'l', 'a', 'l', 'e', 'c', 'c', 'i', 'n', 'n', 'm', 'e', 'r', 'o', 'x', 'p', 'r', 'e', 's', 'i', 'o', 'n', 'e', 's', 'r', 'e', 'g', 'u', 'l', 'a', 'r', 'e', 's']

pattern = r'[0-9]' # todos los números
print(re.findall(pattern, my_string)) # ['7']
print(re.match(pattern, my_string)) # None
print(re.search(pattern, my_string)) # <re.Match object; span=(26, 27), match='7'>

pattern = r'[0-5]' # todos los números del 0 al 5
print(re.findall(pattern, my_string)) # []
print(re.match(pattern, my_string)) # None
print(re.search(pattern, my_string)) # None

pattern = r'\d' # Solo dígitos
print(re.findall(pattern, my_string)) # ['7']

pattern = r'\D' # Que no contenga dígitos
print(re.findall(pattern, my_string)) # ['s', 't', 'a', 'e', 's', 'l', 'a', 'l', 'e', 'c', 'c', 'i', 'n', 'n', 'm', 'e', 'r', 'o', 'x', 'p', 'r', 'e', 's', 'i', 'o', 'n', 'e', 's', 'r', 'e', 'g', 'u', 'l', 'a', 'r', 'e', 's']

pattern = r'[l].' # Solo letras 'L' seguidas de otro caracter
print(re.findall(pattern, my_string)) # ['la', 'le', 'la']

pattern = r'[l].*' # Letras 'L' seguidos de un texto
print(re.findall(pattern, my_string)) # ['la lección número 7: Expresiones regulares']

# email
email = 'sample@email.com' # <== Dirección válida
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+$'
print(re.match(pattern, email)) # <re.Match object; span=(0, 16), match='sample@email.com'>
print(re.search(pattern, email)) # <re.Match object; span=(0, 16), match='sample@email.com'>
print(re.findall(pattern, email)) # ['sample@email.com']

email = 'sample@email-a' # <== Dirección erronea
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+$'
print(re.match(pattern, email)) # None
print(re.search(pattern, email)) # None
print(re.findall(pattern, email)) # []

# https://regex101.com