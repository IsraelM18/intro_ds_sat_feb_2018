############################################################ Tarea 19/02/2019 ################################################

##Ejercicio 18#

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("Tengo nada.")

print_two("Israel","Mendoza")
print_two_again("Israel","Mendoza")
print_one("Primero!")
print_none()



##Ejercicio 19 #

def queso_galletas(queso_count, cajas_galletas):
    print(f"Tienes {queso_count} quesos!")
    print(f"Tienes {cajas_galletas} cajas de galleta!")
    print("Con eso haces una fiesta!")
    print("Conigue una manta.\n")


print("Podemos introducir numeros a la funcion directamente:")
queso_galletas(20, 30)


print("O, podemos usar variables en el script:")
cantidad_de_quesos = 10
cantidad_de_galletas = 50

queso_galletas(cantidad_de_quesos, cantidad_de_galletas)

print("Podemos hacer mate en el interior:")
queso_galletas(10 + 20, 5 + 6)

print("Y podemos combinar ambas, variables y mate:")
queso_galletas(cantidad_de_quesos + 100, cantidad_de_galletas + 1000)



##Ejercicio 20 #

from sys import argv

script, input_file = argv #ValueError: not enough values to unpack (expected 2, got 1)

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)



##Ejercicio 21 #

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")



##Ejercicio 23 #

import sys
script, input_encoding, error = sys.argv
def main(language_file, encoding, errors):

    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)



##Ejercicio 24 #

print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



##Ejercicio 25#

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""

    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
    
    
##Ejercicio 26 #
    
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height=input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv

txt = open(filenme)

print("Here's your file {filename}:")
print(tx.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again_read())


print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
    
    
    
##Ejercicio 28 #
    
True and True
False and True
1 == 1 and 2 == 1
"test" == "test"
1 == 1 or 2 != 1
True and 1 == 1
False and 0 != 0
True or 1 == 1
"test" == "testing"
1 != 0 and 2 == 1
"test" != "testing"
"test" == 1
not (True and False)
not (1 == 1 and 0 != 1)
not (10 == 1 or 1000 == 1000)
not (1 != 10 or 3 == 4)
not ("testing" == "testing" and "Zed" == "Cool Guy")
1 == 1 and (not ("testing" == 1 or 1 == 0))
"chunky" == "bacon" and (not (3 == 4 or 3 == 3))
3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))



##Ejercicio 29#

people = 20
cats = 30
dogs = 15


if people < cats:
    print ("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs + 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")



##Ejercicio 30#

personas = 30
autos = 40
camiones = 15

if autos > personas:
    print("Debemos usar los autos.")
elif autos < personas:
    print("No debemos usar los autos.")
else:
    print("No nos decidimos.")

if camiones > autos:
    print("Hay demasiados camiones.")
elif camiones < autos:
    print("Quiza debamos tomar los camiones.")
else:
    print("Aun no nos decidimos.")

if personas > camiones:
    print("Correcto, simplemente tomemos los camiones.")
else:
    print("Esta bien, entonces nos quedamos en casa.")
    
    
    
##Ejercicio 31#
    
print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
    
    

##Ejercicio 32#
    
la_cuenta = [1, 2, 3, 4, 5]
frutas = ['manzanas', 'naranjas', 'peras', 'chabacano']
cambio = [1,'pennies', 2, 'dimes', 3, 'quarters']

for number in la_cuenta:
    print(f"Esta es la cuenta {number}")
    
for fruta in frutas:
    print("Una fruta de tipo: {}".format(fruta))
    
for i in cambio:
    print("Tengo {}".format(i))


elements = []

for i in range(0, 6):
    print("Adding {} to the list.".format(i))
    elements.append(i)

for i in elements:
    print("Elemento: {}".format(i))
    


##Ejercicio 33#
    
i = 0
numeros = []

i<6

while i < 6:
    print("Al inicio del ciclo: {}.".format(i))
    numeros.append(i) #Itera y va agregando elementos a la lista
    i += 1 #Reemplaza la variable original
    print("El número actual: ", numeros)
    print("Al final del ciclo: {}".format(i))
    
    

##Ejercicio 34#
    
animals = ['bear','tiger','penguin','zebra']
bear = animals [ 0 ]

animales = ['Oso', 'Python3.7' , 'Pavoreal', 'Kanguro', 'Ballena', 'Ornitorrinco']

print("Animal en el 1:",animales[1])
print("El tercer animal:", animales[2])
print("El primer animal:", animales[0] )
print("El animal en el 3:", animales[3])
print("El quinto animal:", animales [4])
print("El animal en el 2:", animales[2])
print("El sexto animal:", animales[5])
print("El animal en el 4:", animales [4])

