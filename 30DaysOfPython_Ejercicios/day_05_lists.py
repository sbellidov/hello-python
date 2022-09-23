# Exercises - Day 5

# Exercises LEVEL 1

# 1 - Declare an empty list
lista_vacia = []
print(lista_vacia)

# 2 - Declare a list with more than 5 items
andalucia = ['Málaga', 'Sevilla', 'Córdoba', 'Granada', 'Cádiz', 'Jaen', 'Huelva', 'Almería']
print(andalucia)

# 3 - Find the length of your list
print(len(andalucia))

# 4 - Get the first item, the middle item and the last item of the list
print(f"Primero: {andalucia[0]}")
print(f"Medio: {andalucia[len(andalucia)//2]}")
print(f"Último: {andalucia[-1]}")

# 5 - Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
persona = ['Sergio', 38, 1.77, 'Divorciado', 'Málaga']
print(persona)

# 6 - Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies= ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7 - Print the list using print()
print(it_companies)

# 8 - Print the number of companies in the list
print(f"Número de compañías: {len(it_companies)}")

# 9 - Print the first, middle and last company
print(f"Primera: {it_companies[0]}")
print(f"Media: {it_companies[len(it_companies)//2]}")
print(f"Última: {it_companies[-1]}")

# 10 - Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print(it_companies)

# 11 - Add an IT company to it_companies
it_companies.append('Twitter')
print(it_companies)

# 12 - Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2,'Spotify')
print(it_companies)

# 13 - Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[2] =it_companies[2].upper()
print(it_companies)

# 14 - Join the it_companies with a string '#;  '
print(' # '.join(it_companies))

# 15 - Check if a certain company exists in the it_companies list.
print(f"Está INDRA en la lista: {it_companies.count('INDRA')>0}")
print(f"Está Amazon en la lista: {it_companies.count('Amazon')>0}")

# 16 - Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17 - Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18 - Slice out the first 3 companies from the list
print(it_companies[0:3])

# 19 - Slice out the last 3 companies from the list
print(it_companies[len(it_companies)-3:])

# 20 - Slice out the middle IT company or companies from the list
print(it_companies[len(it_companies)//2:len(it_companies)//2+1])

# 21 - Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)


# 22 - Remove the middle IT company or companies from the list
it_companies.pop(len(it_companies)//2)
print(it_companies)

# 23 - Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# 24 - Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25 - Destroy the IT companies list
del it_companies
# print(it_companies) # NameError: name 'it_companies' is not defined

# 26 - Join the following lists:
        # front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
        # back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end + back_end)

# 27 - After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end + back_end
print(full_stack.index('Redux'))
full_stack.insert(full_stack.index('Redux'),'Python')
full_stack.insert(full_stack.index('Python'),'SQL')
print(full_stack)

# Exercises LEVEL 2

# 1 - The following is a list of 10 students ages:
#       ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)

#   1.a - Sort the list and find the min and max age
ages.sort()
min = ages[0]
max = ages[-1]
print(f"Min: {min} /// Max: {max}")

#   2.b - Add the min age and the max age again to the list
ages.append(ages[-1])
ages.append(ages[0])
print(ages)

#   2.c - Find the median age (one middle item or two middle items divided by two)
ages.sort()
mediana = ages[len(ages)//2]
print(f"Mediana: {mediana}")

#   2.d - Find the average age (sum of all items divided by their number )
promedio = sum(ages)/len(ages)
print(f"Promedio: {promedio}")

#   2.e - Find the range of the ages (max minus min)
rango = max - min
print(f"Rango (max-min): {rango}")

#   2.f - Compare the value of (min - average) and (max - average), use abs() method
min_avg = abs(min-promedio)
max_avg = abs(max-promedio)
print(f"MIN-AVG = {min_avg}")
print(f"MAX-AVG = {max_avg}")
print(f"La distancia del MIN al AVG es MAYOR QUE la distancia de AVG al MAX ? --> {min_avg > max_avg}")

# 2 - Find the middle country(ies) in the countries list (https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

print(f"Pais en la mediana: {countries[len(countries)//2]}")

# 3 - Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries_list_1 = countries[0:len(countries)//2]
countries_list_2 = countries[len(countries)//2:]
print(f"*** Número de paises en cada lista ***")
print(f"Full list: {len(countries)}")
print(f"Full list: {len(countries_list_1)}")
print(f"Full list: {len(countries_list_2)}")
print(f"Lista 1, primero: {countries_list_1[0]} y último: {countries_list_1[-1]}")
print(f"Lista 2, primero: {countries_list_2[0]} y último: {countries_list_2[-1]}")

# 4 - ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
country_1, country_2, country_3, *scandic = countries
print(country_1)
print(country_2)
print(country_3)
print(scandic)