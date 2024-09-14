#Clase de variables

my_variable = "My string variable"
print(my_variable)

# Examples
first_name = 'Asabeneh'  #str
last_name = 'Yetayeh'    #str
country = 'Finland'
city = 'Helsinki'
age = 250                #int
is_married = True        #boolean
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']   #list
person_info = {           #dict
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }

print(first_name, last_name, city, skills, person_info)

# Para saber la longitud de una variable utilizamos la funcion len()
print(len(city))

# Multiple variables can also be declared in one line:  NO ABUSAR DE ESTA SINTAXIS!!
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True
print(first_name, last_name, country, age, is_married)

# Getting user input using the input() built-in function. Let us assign the data we get from a user into first_name and age variables. Example:

first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)