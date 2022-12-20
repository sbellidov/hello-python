### Python Package Manager ###

# PIP (https://pypi.org/project/pip/)

# En la terminal ejecutar 'pip install pip'

# pip install numpy
import numpy

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))
print(numpy_array * 2)

# pip install pandas
import pandas


# pip list

# Package         Version
# --------------- -------
# numpy           1.24.0
# pandas          1.5.2
# pip             22.3.1
# python-dateutil 2.8.2
# pytz            2022.7
# setuptools      63.2.0
# six             1.16.0
# wheel           0.38.4


# pip uninstall pandas
# ==> Successfully uninstalled pandas-1.5.2


# pip show numpy

#   Name: numpy
#   Version: 1.24.0
#   Summary: Fundamental package for array computing in Python
#   Home-page: https://www.numpy.org
#   Author: Travis E. Oliphant et al.
#   Author-email: 
#   License: BSD-3-Clause
#   Location: /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages
#   Requires: 
#   Required-by: 

import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
print(response)
print(response.status_code)
print(response.json())


# Arithmetics Package
from mypackage import arithmetics
print(arithmetics.sum_two_values(1, 4))


# Webbrowser
import webbrowser

url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# Abre la lista de websites en nuevas pestañas
for url in url_lists:
    webbrowser.open_new_tab(url)