
# Python Error Types

# When we write code it is common that we make a typo or some other common error. If our code fails to run, the Python interpreter will display a message, containing feedback with information on where the problem occurs and the type of an error. It will also sometimes gives us suggestions on a possible fix. Understanding different types of errors in programming languages will help us to debug our code quickly and also it makes us better at what we do.

# Let us see the most common error types one by one. First let us open our Python interactive shell. Go to your you computer terminal and write 'python'. The python interactive shell will be opened.
# SyntaxError

# Example 1: SyntaxError

# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print 'hello world'
#   File "<stdin>", line 1
#     print 'hello world'
#                       ^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
# >>>

# As you can see we made a syntax error because we forgot to enclose the string with parenthesis and Python already suggests the solution. Let us fix it.

# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print 'hello world'
#   File "<stdin>", line 1
#     print 'hello world'
#                       ^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
# >>> print('hello world')
# hello world
# >>>

# The error was a SyntaxError. After the fix our code was executed without a hitch. Let see more error types.
# NameError

# Example 1: NameError

# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print(age)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'age' is not defined
# >>>

# As you can see from the message above, name age is not defined. Yes, it is true that we did not define an age variable but we were trying to print it out as if we had had declared it. Now, lets fix this by declaring it and assigning with a value.

# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print(age)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'age' is not defined
# >>> age = 25
# >>> print(age)
# 25
# >>>

# The type of error was a NameError. We debugged the error by defining the variable name.
# IndexError

# Example 1: IndexError

# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> numbers = [1, 2, 3, 4, 5]
# >>> numbers[5]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
# >>>

# In the example above, Python raised an IndexError, because the list has only indexes from 0 to 4 , so it was out of range.
# ModuleNotFoundError

# Example 1: ModuleNotFoundError

# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import maths
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'maths'
# >>>

# In the example above, I added an extra s to math deliberately and ModuleNotFoundError was raised. Lets fix it by removing the extra s from math.

# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import maths
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'maths'
# >>> import math
# >>>

# We fixed it, so let's use some of the functions from the math module.
# AttributeError

# Example 1: AttributeError

# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import maths
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'maths'
# >>> import math
# >>> math.PI
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'math' has no attribute 'PI'
# >>>

# As you can see, I made a mistake again! Instead of pi, I tried to call a PI function from maths module. It raised an attribute error, it means, that the function does not exist in the module. Lets fix it by changing from PI to pi.

# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import maths
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'maths'
# >>> import math
# >>> math.PI
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'math' has no attribute 'PI'
# >>> math.pi
# 3.141592653589793
# >>>

# Now, when we call pi from the math module we got the result.
# KeyError

# Example 1: KeyError

# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
# >>> users['name']
# 'Asab'
# >>> users['county']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'county'
# >>>

# As you can see, there was a typo in the key used to get the dictionary value. so, this is a key error and the fix is quite straight forward. Let's do this!

# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> user = {'name':'Asab', 'age':250, 'country':'Finland'}
# >>> user['name']
# 'Asab'
# >>> user['county']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'county'
# >>> user['country']
# 'Finland'
# >>>

# We debugged the error, our code ran and we got the value.
# TypeError

# Example 1: TypeError

# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 4 + '3'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# >>>

# In the example above, a TypeError is raised because we cannot add a number to a string. First solution would be to convert the string to int or float. Another solution would be converting the number to a string (the result then would be '43'). Let us follow the first fix.

# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 4 + '3'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# >>> 4 + int('3')
# 7
# >>> 4 + float('3')
# 7.0
# >>>

# Error removed and we got the result we expected.
# ImportError

# Example 1: TypeError

# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from math import power
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: cannot import name 'power' from 'math'
# >>>

# There is no function called power in the math module, it goes with a different name: pow. Let's correct it:

# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from math import power
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: cannot import name 'power' from 'math'
# >>> from math import pow
# >>> pow(2,3)
# 8.0
# >>>

# ValueError

# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> int('12a')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '12a'
# >>>

# In this case we cannot change the given string to a number, because of the 'a' letter in it.
# ZeroDivisionError

# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 1/0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
# >>>

# We cannot divide a number by zero.

# We have covered some of the python error types, if you want to check more about it check the python documentation about python error types. If you are good at reading the error types then you will be able to fix your bugs fast and you will also become a better programmer.

# 🌕 You are excelling. You made it to half way to your way to greatness. Now do some exercises for your brain and for your muscle.
# 💻 Exercises: Day 15

#     Open you python interactive shell and try all the examples covered in this section.

# 🎉 CONGRATULATIONS ! 🎉

# << Day 14 | Day 16 >>



# CODIGO DE BRAIS MOURE

# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=12721

### Error Types ###

# SyntaxError
# print "¡Hola comunidad!"   # Descomentar para Error
#output
# File "/Users/andme/Develmnt/MoureDev/Python-Intermediate/05_error_types.py", line 293
#     print "¡Hola comunidad!"
#     ^^^^^^^^^^^^^^^^^^^^^^^^^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?


from math import pi
import math
print("¡Hola comunidad!")

# NameError
language = "Spanish"  # Comentar para Error
print(language)
# output
# Traceback (most recent call last):
#   File "/Users/andme/Develmnt/MoureDev/Python-Intermediate/05_error_types.py", line 307, in <module>
#     print(language)
#           ^^^^^^^^
# NameError: name 'language' is not defined


# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
# print(my_list[5]) # Descomentar para Error

# ModuleNotFoundError
# import maths # Descomentar para Error

# AttributeError
# print(math.PI) # Descomentar para Error
print(math.pi)

# KeyError
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
print(my_dict["Edad"])
# print(my_dict["Apelido"]) # Descomentar para Error
print(my_dict["Apellido"])

# TypeError
# print(my_list["0"]) # Descomentar para Error
print(my_list[0])
print(my_list[False])

# ImportError
# from math import PI # Descomentar para Error
print(pi)

# ValueError
#my_int = int("10 Años")
my_int = int("10")  # Descomentar para Error
print(type(my_int))

# ZeroDivisionError
# print(4/0) # Descomentar para Error
print(4/2)


