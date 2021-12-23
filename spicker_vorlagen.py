# Comments
# One Line Comment
'''Multiline
Comment'''

#Operatoren
print(2 + 3 * 6)
print((2 + 3) * 6)
print(2 ** 8)
print(23 // 7)
print(23 % 7)
print((5 - 1) * ((7 + 1) / (3 - 1)))

# String concatination
print('Alice' 'Bob')
print('Alice' * 5)

# Variablen _spam should not be used again in the code.
_internal = 'Hello'
__private = 'Hell0'
spam = 'Hello'
x,y = 2,3
x = y = z = 30
x,*y,z= 1,2,2.5,3,4
print(y)

# Variable names
bob = Bob = _bob = _2_bob_= bob_2 = BoB = 'Bob'
# not allowed 2bob /bob boB*b 

# Functions
# Numbers
print(str(29))
print(int(7.7))
print(round(2.77777,2))
print(type(1))
# Strings
myName = 'name'
print('It is good to meet you, {}'.format(myName))
print(len('hello'))
print(f'Die Summe ist: {2+3}')
tname = 'Robinson Crusoe'
print(tname[5:8])
print(tname[:8])
print(tname[9:])
test = 'Das ist ein Beispiel'
print(test.count('ei')) 
print(test.find('ei'))
print(test.find('ei',9))
print(test.rfind('ei'))
print(test.replace('ist', 'war'))

# Lists / Besteht aus unterschiedlichen Objekttypen und ist veränderbar
liste = [0,1,2,3]
print(len(liste))
print(sum(liste))
print(max(liste))
print(min(liste))
liste.insert(0,5)
liste.append(4)
liste.sort()
print(liste)
liste.reverse()
print(liste)
# Remove Value
liste.remove(2)
# Remove by index
del liste[1]
# Provides index and element
for index, element in enumerate(liste):
    print(index, element)

mehr_dimensionale_liste =[['Paris','Fr',350000],['Rom','It',420000]]
mehr_dimensionale_liste[0][1] = 'CH'
print(mehr_dimensionale_liste[0][1])


# Tupel / Tupel kann nicht verändert warden
tup = (1,1,2,3,4,4)
# Counts how often 
print(tup.count(1))
# Provides index of given element
print(tup.index(1))
print(tup)

# Dictionarys / Schlüssel und Wert Paare und sind veränderbar
dictionary = {'schlüssel1': 23, 'schlüssel2': 24, 'schlüssel3':25}
dictionary['schlüssel1'] = 32
del dictionary['schlüssel2']
print(dictionary)
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# Removes by key
dictionary.pop('schlüssel1')
# Get value by key
print(dictionary.get('schlüssel3'))
# updates value, when not exists it creates key & value
dictionary.update({'schlüssel1': 21})
# Removes last item
dictionary.popitem();
print(dictionary)

# Sets / Sets dürfen Elemente NUR ein mal vorkommen und sind geordnet
s1 = set([5,5,6,6,1,2,2,3,3,4])
s2 = s1.copy()
s2.add(10)
# Removes when exists, raises no error
s1.discard(1)
s1.update([7,8])
# Removes, when not exists raises error
s1.remove(8)
# Removes first item
s1.pop()
print(s1)
print(s1 < s2)
# Vereinigungsmenge
print(s1| s2)
print(s1.union(s2))
# Schnittmenge
print(s1&s2)
print(s1.intersection(s2))
# Symetrische Differenz
print(s1 ^ s2)
print(s1.symmetric_difference(s2))
# Differenzmenge
print(s2 -s1)
print(s2.difference(s1))
s1.clear()
print(s1)

# Comparison Operators
print(42 == 42)
print(42 != 42)
print(42 > 42)  
print(42 >= 42)
print(42 < 42)  
print(42 <= 42)
print(True is not False)
print(not False)
print(True and True)
print(True or False)

# None / The None keyword is used to define a null value, or no value at all.
print(not None)
# if, elif else
name = 'Bob'
age = 30
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')
spam = 'old' if age > 18 else 'young'
print(spam)

# while / unbounded number of  iterations can also use break but not continues
spam = 0
while spam < 5:
    if (spam == 4):
        break
    print(spam)
    spam = spam + 1

# for / know number of  iterations / 
for i in range(0,10):
    if i == 1: continue
    if i == 7: break
    print(i)
for i in range(10, 0, -2):
    print(i)

# try, except, else, finally with function
def devide(first, second):
    try:
        first / second
        print(first / second)
    except ZeroDivisionError as e:
        print('Error: Invalid argument: {}'.format(e))
    else:
        print('Nothing went wrong')
    finally:
        print('division finished')
devide(31,1)

#Number
print('Dezimal', 5)
print('Dual 5', bin(5))
print('Dual 6', bin(6))
print('Calculations', bin(5 & 6), bin(5 | 6), bin(5 + 6))
print('Oktal 5', oct(5))
print('Oktal 6', oct(6))
print('Calculations', oct(5 & 6), oct(5 | 6), oct(5+6))
print('Hexadezimal', hex(31), hex(21))

# Math
import math
print(math.log(4,2))
print(math.sqrt(4))
print(math.pow(2,3))
print(math.pi)
print(math.e)

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
# from os import *
# exec('print(dir())')

# string format
# Zahlen mit Nachkommastellen
x = 100/7
y = 2/7
print("Zahlen:", x, y)
# Format e
print(f"Format e Standard: {x:e} {x:e} {y:e}")
print(f"Format e, nach Komma: {x:.3e}")
print(f"Format e, gesamt: {x:12.3e}")
# format f
print(f"Format f, Standard: {x:f} {x:f} {y:f}")
print(f"Format f, nach Komma: {x:.25f}")
print(f"Format f, gesamt: {x:15.10f}" )
# Format %
print(f"Format % Standard: {x:%} {y:%}")
print(f"Format %, nach Komma: {y:.3%}")
print(f"Format %, gesamt: {y:12.3%}")
# Tabelle mit verschiedenen Objekten
artname ={23:"Apfel",8:"Banane",42:"Pfirsisch"}
anzahl ={23:1, 8:3, 42:5}
epreis ={23:2.95, 8:1.45, 42:3.05}
print(f"{'Nr':>4}{'Name':>12}{'Anz':>4}{'EP':>13}{'GP':>13}")
for x in 23, 8, 42:
    print(f"{x:04d}{artname[x]:>12}{anzahl[x]:4d}{epreis[x]:8.2f} Euro {anzahl[x]*epreis[x]:8.2f} Euro")
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
    value /=2
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

# OOP
class Person():
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    def __str__(self) -> str: return f'{self.name} ist {self.alter} Jahre alt' 
    
    def display(self) -> str: return f'{self.name} ist {self.alter} Jahre alt'
mischa = Person('Mischa', 24)
print(mischa)
class Student(Person):
    def __init__(self, name, alter, modul):
        super().__init__(name, alter)
        self.modul = modul;
    def display(self) -> str:
        return f'{self.name} ist {self.alter} Jahre alt und besucht das Modul {self.modul}'

student = Student('Mischa', 24, 'Python')
print(student.display())
class Car:
    def __init__(self, color='pink', mileage=1, name='Car', speed=1):
        self.color = color
        self.mileage = mileage
        self.name = name
        self.speed = speed
    def __str__(self) -> str:
        return f'The {self.name} drives at {self.speed} km/h'
    def __eq__(self, __o: object) -> bool: return  self.name == __o.name
    def __gt__(self, __o: object) -> bool: return self.mileage > __o.mileage
    def __sub__(self, __o: object) -> int: return self.mileage - __o.mileage
    def __ge__(self, __o :object) -> bool: return self.mileage >= __o.mileage
    def __lt__(self, __o: object) -> bool: return self.mileage < __o.mileage
    def __le__(self, __o: object) -> bool: return self.mileage <= __o.mileage
    def __ne__(self, __o: object) -> bool: return self.mileage != __o.mileage
    def accelerate(self, newSpeed):
        self.speed += newSpeed
# Custom non reference copmaring   
red = Car('red', 20000)
blue = Car('blue', 30000)
print(red)
print(blue)
print(red == blue)
print(red < blue)
print(red - blue)

# copy vs deepcopy
import copy
original = Car(name='A3', speed=100)
copy1 = copy.copy(original)
copy1.accelerate(11)
deepCopy1 = copy.deepcopy(original)
deepCopy1.name = 'A1'
original1 = original
original.accelerate(15)

print(original)
print(copy1)
print(deepCopy1)
print(original1)
print(original is original1)
print(original is copy1)
print(original is deepCopy1)

# dataclass
from dataclasses import dataclass
import math
@dataclass
class Point():
    x: float = 0.0
    y: float = 0.0
    
    def move(self, x ,y) -> None:
        self.x = x
        self.y = y
        
    def distance(self, __point: object) -> float:
        return math.sqrt((self.x - __point.x)**2 + (self.y - __point.y)**2)

point = Point(1,2)
point2 = Point(3,4)
distance = point.distance(point2)
# With 3 after comma
print(f'{distance:.3f}')
print(point)
point.move(2,3)
print(point)



# Examples
def hello(name):
     return 'Hello {}'.format(name)
print(hello('mischa'))

def docs():
    """Mein neuer Kommentar"""
    print('Hallo')
print(docs.__doc__)

# Max Calculator
def max_of_three(x: int,y: int,z: int) -> int:
    return max([x,y,z])
print(max_of_three(-1,5,3))

# Quersummenrechner
def Quersumme(num):
    return sum(i + 1 for i in range(num))
print(Quersumme(10))

from typing import List
import random

class SparseVector():
    def __init__(self, dimension: int, nonzeroValues: List[int], nonzeroIndexes: List[int]):
        self.dimension = dimension
        self.nonzeroValues = nonzeroValues
        self.nonzeroIndexes = nonzeroIndexes
    # benutzerfreundliche Darstellung des Objektes als String ausgibt wie folgt, in kompakt und vollständiger Schreibweise wie oben beschrieben
    def __str__(self):
        return f'Kompakte Schreibweise: {self.getVectorCompact()} \nVollständige Schreibweise: {self.getVectorWithZeroValues()}'
    # gibt dimension des Vektors zurück 
    def getDimension(self):
        return self.dimension
    # gibt nonzeroValues zurück
    def getNonzeroValues(self):
        return self.nonzeroValues
    # gibt nonzeroIndexes zurück
    def getNonzeroIndexes(self):
        return self.nonzeroIndexes
    # Erstellt dictionary um kompakte schreibweise darzustellen.
    def getVectorCompact(self):
        zip_iterator = zip(self.nonzeroIndexes, self.nonzeroValues)
        return dict(zip_iterator)
    # Erstellt Liste um vollständige reibweise darzustellen.
    def getVectorWithZeroValues(self):
        vector = []
        for index in range(1, self.dimension + 1):
            non_zero_value = self.getNonzeroValueByIndex(index)
            if (non_zero_value is not None):
                vector.append(non_zero_value)
            else:
                vector.append(0)
        return vector 
    # überprüft, ob index i kleiner als dimension und positiv ist, dann Vektorelement mit index i, diesen Wert(value) erhalten
    # Früher setNonzeroValue(value, index)
    def getNonzeroValueByIndex(self, index: int):
        if (self.dimension < index or index <= 0):
            return None
        if (index in self.nonzeroIndexes):
            i = self.nonzeroIndexes.index(index)
            return self.nonzeroValues[i]
        else:
            return None
        
    #  multipliziert den Vektor mit einem factor
    def multiply(self, factor: float):
        multiplied_vector = []
        for value in self.nonzeroValues:
            multiplied_vector.append(value * factor)
        return multiplied_vector

# welche aus den zwei Sparse-Vektoren a und b die Summe bildet und diesen als neues Sparse-Objekt zurückgibt.
def addSparse(sparse_vector1: SparseVector, sparse_vector2: SparseVector) -> SparseVector:
    summed_vector = list(map(lambda x, y: x + y, sparse_vector1.getVectorWithZeroValues(), sparse_vector2.getVectorWithZeroValues()))
    non_zero_indexes = []
    non_zero_values = []
    for index, value in enumerate(summed_vector):
        if (value != 0):
            non_zero_indexes.append(index + 1)
            non_zero_values.append(value)
    return SparseVector(len(summed_vector), non_zero_values, non_zero_indexes) 

# welche das Skalarprodukt der beiden Sparse-Vektoren berechnet und zurückgibt.
def dotSparse(sparse_vector1: SparseVector, sparse_vector2: SparseVector) -> int:
    vector1 = sparse_vector1.getVectorWithZeroValues()
    vector2 = sparse_vector2.getVectorWithZeroValues()
    if len(vector1) != len(vector2):
        return 0
    # Erstellt tupels mit (a1, b1),(a2,b2) etc.
    zipped_vector = zip(vector1, vector2)
    return sum(i[0] * i[1] for i in zipped_vector)

# Dimension n, höchstens m von Null verschiedene Einträge, deren Wert im Intervall [a,b] liegen.
def createRandomSparse(dimension: int, max_non_zero_values: int, start: int, end: int) -> SparseVector:
    non_zero_indexes = []
    non_zero_values = []
    while True:
        index = random.randint(1, dimension)
        value = random.randint(start, end)
        if (index not in non_zero_indexes):
            non_zero_indexes.append(index)
            non_zero_values.append(value)
        if (len(non_zero_indexes) == max_non_zero_values): break
    return SparseVector(dimension, non_zero_values, sorted(non_zero_indexes))  