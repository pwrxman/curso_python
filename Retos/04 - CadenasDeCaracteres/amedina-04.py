

"""
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 """

# Creating a string
letter="P"
string="My string"
hello="Hello World!!"
print(letter)
print(string)
print(hello)


multiline_string="""this is an example of a string divided in several lines.
The power of you is coming from inside of you.
The life is great, enjoy it!!"""
print(multiline_string)

# string concatenation
name="Andrei"
last_name=("Med")
full_name=name+" "+last_name

# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# string interpolation
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')

# Sequence of characters
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

# String index normal from 0 to the end
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

# String index inverse order the end to -len
language = 'Python'
last_letter = language[-1]
print(f"\n{last_letter}") # n
second_last = language[-2]
print(second_last) # o
print(language[-len(language)])

# Reversing a String
hello = 'Hello, World!'
print(hello[::-1]) 

# substrings
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto

# Methods
phrase="the world is ours, enjoy it!"

# Convert first character Upper
print(phrase.capitalize(), "\n")

# count(substring, start=.., end=..). 
# Returns the number of times a specified value occurs in a string. 
# The start is a starting indexing for counting and end is the last index to count.
# return 0 if not found
print(phrase.count('w')) 
print(phrase.count('ld', 7, 14)) 
print(phrase.count('x'))

# find(): Returns the index of the first occurrence of a substring, if not found returns -1
print("\n", phrase.find('ours'))
print(phrase.find('the'))
print(phrase.find('xx'))

# format(): formats string into a nicer output
radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print("\n", result) # The area of a circle with radius 10 is 314

# isalnum()	Returns True if all characters in the string are alphanumeric
phrase="No pain no gain"
print("\n", phrase.isalnum())
phrase="Pele won 5 futbol wold championships"
print("\n", phrase.isalnum())

# isalpha()	Returns True if all characters in the string are in the alphabet
phrase = 'Las clases de Moure'
print(phrase.isalpha()) # False, space is excluded
phrase = 'LasclasesdeMoure'
print(phrase.isalpha()) 
num = '85478'
print(num.isalpha()) 

# isdecimal()	Returns True if all characters in the string are decimals '0123456789'
phrase = 'thirty'
print(phrase.isdecimal())
phrase = '69587'
print(phrase.isdecimal()) 
phrase = '3.1416'
print(phrase.isdecimal())

# isdigit()	Returns True if all characters in the string are digits 0123456789 other unicode characters for numbers) 
phrase = 'Thirty'
print(phrase.isdigit())
phrase = '53489'
print(phrase.isdigit())
phrase = '\u00B2'
print(phrase.isdigit())

# islower()	Returns True if all characters in the string are lower case
phrase = 'Los cursos de Moure'
print(phrase.islower()) 
phrase = 'las clases de python'
print(phrase.islower())

# isupper()	Returns True if all characters in the string are upper case
phrase = 'Los cursos de Moure'
print(phrase.isupper()) 
phrase = 'THE COURSE OF PYTHON'
print(phrase.isupper()) 


# strip()	Returns a trimmed version of the string
phrase = 'thirty days of vacationnn'
print("\n", phrase.strip('nothdv')) 


# upper()	Converts a string into upper case
print(phrase.upper())

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos    Palabra o frase que se lee identicamente en ambos sentidos
 * - Anagramas      Palabra o frase con las mismas letras pero con distinto significado
 * - Isogramas      Palabra o frase en la que ninguna letra del alfabeto aparece más de una vez.
                    Palabra o frase en la que cada letra aparece el mismo número de veces. ​ 
                    Si cada letra aparece solo una vez será un heterograma, 
                    si aparece dos, un isogroma de segundo orden y así sucesivamente
 """