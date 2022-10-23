# Exercises - Day 12
'''
# Exercises: Level 1

# 1 - Write a function which generates a six digit/character random_user_id.
#       print(random_user_id());
#       '1ee33d'
def random_user_id():
    import string
    import random
    random_user_id = []
    for i in range(6):
        random_user_id.append(random.choice(string.ascii_letters + string.digits))
    return ''.join(random_user_id)

print(random_user_id())


# 2 - Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input().
#  One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
#       print(user_id_gen_by_user()) # user input: 5 5
#       #output:
#       #kcsy2
#       #SMFYb
#       #bWmeq
#       #ZXOYh
#       #2Rgxf
#
#       print(user_id_gen_by_user()) # 16 5
#       #1GCSgPLMaBAVQZ26
#       #YD7eFwNQKNs7qXaT
#       #ycArC5yrRupyG00S
#       #UbGxOFI7UXSWAyKN
#       #dIV0SSUTgAdKwStr

from logging import exception


def user_id_gen_by_user():
    import string
    import random
    user_input = input()
    length = user_input.split(' ')[0]
    qty = user_input.split(' ')[1]

    try:
        length = int(length)
        qty = int(qty)
    except ValueError as error:
        print(error)

    for i in range(qty):
        random_user_id = []
        for j in range(length):
            random_user_id.append(random.choice(string.ascii_letters + string.digits))
        print(''.join(random_user_id))

user_id_gen_by_user()

'''

# 3 - Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
#       print(rgb_color_gen())
#       # rgb(125,244,255) - the output should be in this form
def rgb_color_gen():
    import random
    rgb = []
    for i in range(3):
        rgb.append(random.randint(0,255))
    return(f"rgb({rgb[0]},{rgb[1]},{rgb[2]})")

print(rgb_color_gen())

# Exercises: Level 2
# 1 - Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #.
# Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

def list_of_hexa_colors(total_colors = 1):
    import random
    import string
    list_of_colors = []
    for i in range(total_colors):
        #list_of_colors.append('#'+''.join(random.choices(range(10),k=6)))
        list_of_colors.append('#'+''.join(random.choices(string.digits + 'abcdef',k=6)))
    return list_of_colors

print(list_of_hexa_colors(10))


# 2 - Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(total_colors = 1):
    import random
    list_of_colors = []
    for i in range(total_colors):
        list_of_colors.append(rgb_color_gen())
    return list_of_colors

print(list_of_rgb_colors(3))


# 3 - Write a function generate_colors which can generate any number of hexa or rgb colors.
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']

def generate_colors(format,qty):
    if format == 'hexa':
        return list_of_hexa_colors(qty)
    elif format == 'rgb':
        return list_of_rgb_colors(qty)
    else:
        return 'Formato de color debe ser *hexa* o *rgb*'

print(generate_colors('hexa',3))
print(generate_colors('hexa',1))
print(generate_colors('rgb',3))
print(generate_colors('rgb',1))



# Exercises: Level 3
# 1 - Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lista):
    import random
    shuffle_list = random.shuffle(lista)
    return shuffle_list

lista_1 = ['a','h','t','r','v','d','e']
lista_2 = [8,6,4,5,3,0,7]
print(lista_1)
print(lista_2)
shuffle_list(lista_1)
shuffle_list(lista_2)
print(lista_1)
print(lista_2)


# 2 - Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def array_of_seven_uniques():
    import random
    result = []
    while len(result) < 7:
        new_value = random.randrange(10)
        if new_value not in result:
            result.append(new_value)
    return result

print(array_of_seven_uniques())