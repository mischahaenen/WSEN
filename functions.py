# Input mit paramatern
Summe = 0
for i in range (1,4):
    fehler = True
    while fehler:
        try:
            #zahl = input(f"${i} Zahl eingeben: ")
            #Summe += float(zahl)
            fehler = False
        except:
            print("keine Zahl")
            fehler = True
            print("Summe: ", Summe) 
            
# pass -> führt code aus ohne implementation zu schreiben ohne pass funktioniert spam() nicht.
def spam():
    pass

#eval() evaluiert den zusammengestzten Ausdruck and returns its value
number = 9
# eval performs the multiplication passed as argument
square_number = eval('number * number')
print(square_number)
# Perimeter of Square
def calculatePerimeter(l):
    return 4*l
# Area of Square
def calculateArea(l):
    return l*l
expression = 'calculatePerimeter(l)' #input("Type a function: ") 
for l in range(1, 5):
    if (expression == 'calculatePerimeter(l)'):
        print("If length is ", l, ", Perimeter = ", eval(expression))
    elif (expression == 'calculateArea(l)'):
        print("If length is ", l, ", Area = ", eval(expression))
    else:
        print('Wrong Function')
        break
""" eval vs exec: Basically, eval is used to evaluate a single dynamically generated Python expression,
and exec is used to execute dynamically generated Python code only for its side effects. """

#exec() führt eine zusammengestzte Anweisung aus: exec() doesn't return any value, it returns None.
program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)
# dangerous example
from os import *
exec('print(dir())')

# modulo
x = -12
y= 15
# Ausdruck zur Zuweisung
maximum = x if x > y else y
print(maximum)
# Ausdruck zur Ausgabe
print("positiv" if x>0 else "negativ oder 0")
# ZIP -> erstellt tuples aus lists
plz = [49808, 78224, 55411]
stadt = ["Lingen", "Singen", "Bingen"]
bundesland = ["NS", "BW", "RP"]
#zip() verbindet die Objekte
kombi = zip(plz, stadt, bundesland)
for element in kombi:
    print(element)

# MAP -> The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns an iterator.
numbers = [2, 4, 6, 8, 10]
# returns square of a number
def square(number):
  return number * number
# apply square() function to each item of the numbers list
squared_numbers_iterator = map(square, numbers)
# converting to list
squared_numbers = list(squared_numbers_iterator)
print(squared_numbers)

# FILTER -> function extracts elements from an iterable (list, tuple etc.) for which a function returns True.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# returns True if number is even
def check_even(number):
    if number % 2 == 0:
          return True  
    return False
# Extract elements from the numbers list for which check_even() returns True
even_numbers_iterator = filter(check_even, numbers)
# converting to list
even_numbers = list(even_numbers_iterator)
print(even_numbers)

# Variable Parameters with *
def summe(*summand):
    print(summand)
    return(len(summand))
print(summe(1,2,3,4,4))

# Named parameters
def volume(width, length, depth=2, color="red"):
    print("dimensions: ", width, length, depth, color)
    vol = width * length * depth
    print("Volume : ", vol, "color: ", color)
# Reihenfolge muss nicht beachtet werden, wenn namen verwendet werden
volume(4,8, color = "pink")

# Mehrere Rückgabewerte
import math
def circle (r):
    area = math.pi *r **2
    circumference = 2* math.pi * r
    return area, circumference
flaeche, hoehe = circle(9)
print(flaeche, hoehe)

# global, local
eggs = 'white'
def spam():
    global eggs
    eggs = 'yellow'
spam()
print(eggs)

# Recursive Functions
def half(value):
    print(value)
    value /= 2
    if value >0.005:
        half(value)
    return value
v=half(5)

# lamdda
mal = lambda x,y: x*y
div = lambda x,y: x/y
plus= lambda x,y: x+y
minus = lambda x,y: x-y
print(mal(2,4))
print(div(2,4))
print(plus(2,4))
print(minus(2,4))

# function as parameter
square = lambda x:x * x
# and passing function as an argument
cube = lambda func:func**3
print("square of 2 is :", square(2))
print("The cube of ", square(2), " is " + str(cube(square(2))))
