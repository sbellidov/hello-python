# Exercises - Day 4

# 1 - Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
str1 = 'Thirty'
str2 = 'Days'
str3 = 'Of'
str4 = 'Python'
print("{} {} {} {}".format(str1,str2,str3,str4))
print(f"{str1} {str2} {str3} {str4}") # A partir de Python 3.6

# 2 - Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
str1 = 'Coding'
str2 = 'For'
str3 = 'All'
print(f'{str1} {str2} {str3}')

# 3 - Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

# 4 - Print the variable company using print().
print(company)

# 5 - Print the length of the company string using len() method and print().
print(f"Length: {len(company)}")

# 6 - Change all the characters to uppercase letters using upper() method.
print(f"upper: {company.upper()}")

# 7 - Change all the characters to lowercase letters using lower() method.
print(f"lower: {company.lower()}")

# 8 - Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(f"capitalize: {company.capitalize()}")
print(f"title: {company.title()}")
print(f"swapcase: {company.swapcase()}")

# 9 - Cut(slice) out the first word of Coding For All string.
print(company[0:6])

# 10 - Check if Coding For All string contains a word Coding using the method index, find or other methods.
substring = 'Coding'
print(f"La cadena: '{company}' contiene la cadena: '{substring}' -->> { company.find(substring) > -1 } ")

# 11 - Replace the word coding in the string 'Coding For All' to Python.
print(f"{company.replace('Coding','Python')}")
print(company)

# 12 - Change 'Python for Everyone' to 'Python for All' using the replace method or other methods.
print('Python for Everyone'.replace('Everyone','All'))

# 13 - Split the string 'Coding For All' using space as the separator (split()) .
print('Coding For All'.split(' '))

# 14 - "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(', '))

# 15 - What is the character at index 0 in the string Coding For All.
print('Coding For All'[0]) # 'C'

# 16 - What is the last index of the string Coding For All.
print('Coding For All'[-1]) #'l'

# 17 - What character is at index 10 in "Coding For All" string.
print('Coding For All'[10]) #' '

# 18 - Create an acronym or an abbreviation for the name 'Python For Everyone'.
string = "Python For Everyone"
print(string.split(' ')[0][0] + string.split(' ')[1][0] + string.split(' ')[2][0]) #PFE

# 19 - Create an acronym or an abbreviation for the name 'Coding For All'.
string = "Coding For All"
print(string.split(' ')[0][0] + string.split(' ')[1][0] + string.split(' ')[2][0]) #CFA

# 20 - Use index to determine the position of the first occurrence of C in Coding For All.
print('Coding For All'.index('C')) #0

# 21 - Use index to determine the position of the first occurrence of F in Coding For All.
print('Coding For All'.index('F')) #7

# 22 - Use rfind to determine the position of the last occurrence of l in Coding For All People.
print('Coding For All'.rfind('l')) #13

# 23 - Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

# 24 - Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))

# 25 - Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence[sentence.find('because'):sentence.rindex('because')+len('because')]) # Desde la 1ª aparición hasta la 2ª + la longitud de la palabra

# 26 - Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

# 27 - Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence[sentence.find('because'):sentence.rindex('because')+len('because')])

# 28 - Does ''Coding For All' start with a substring Coding?
print('\'Coding For All'.startswith('Coding')) # El símbolo ' hace que no coincida

# 29 - Does 'Coding For All' end with a substring coding?
print('Coding For All'.startswith('coding')) # Sensible a mayúsculas/minúsculas

# 30 - '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      '.strip())

# 31 - Which one of the following variables return True when we use the method isidentifier():
#       30DaysOfPython
#       thirty_days_of_python
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# 32 - The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(list))

# 33 - Use the new line escape sequence to separate the following sentences.
#       I am enjoying this challenge.
#       I just wonder what is next.
print('I am enjoying this challenge\nI just wonder what is next')

# 34 - Use a tab escape sequence to write the following lines.
#       Name      Age     Country   City
#       Asabeneh  250     Finland   Helsinki
print('Name\t\tAge\tCountry\t\tCity')
print('Asabeneh\t250\tFinland\t\tHelsinki')

# 35 - Use the string formatting method to display the following:
#       - radius = 10
#       - area = 3.14 * radius ** 2
#       - The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {:d} is {:0.0f} meters square'.format(radius,area)) # Float sin decimales -> {:0.0f}

# 36 - Make the following using string formatting methods:
#       8 + 6 = 14
#       8 - 6 = 2
#       8 * 6 = 48
#       8 / 6 = 1.33
#       8 % 6 = 2
#       8 // 6 = 1
#       8 ** 6 = 262144
print('8 + 6 = {}'.format( 8 + 6 ))
print('8 - 6 = {}'.format( 8 - 6 ))
print('8 * 6 = {}'.format( 8 * 6 ))
print('8 / 6 = {:0.2f}'.format( 8 / 6 ))
print('8 % 6 = {}'.format( 8 % 6 ))
print('8 // 6 = {}'.format( 8 // 6 ))
print('8 ** 6 = {}'.format( 8 ** 6 ))