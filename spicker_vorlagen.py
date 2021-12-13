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

# functions
def hello(name):
     return 'Hello {}'.format(name)
print(hello('mischa'))

# Variable Parameters with *
def summe(*summand):
    print(summand)
    return(len(summand))
print(summe(1,2,3,4,4))

def volume(width, length, depth=2, color="red"):
    print("dimensions: ", width, length, depth, color)
    vol = width * length * depth
    print("Volume : ", vol, "color: ", color)
#testen
volume(4,8,9,"green")
volume(4,8,9)
volume(4,8)
# Reihenfolge muss nicht beachtet werden, wenn namen verwendet werden
volume(4,8, color = "pink")

eggs = 'white'
def spam():
    global eggs
    eggs = 'yellow'
spam()
print(eggs)

def docs():
    """Mein neuer Kommentar"""
    print('Hallo')

print(docs.__doc__)

# Max Calculator

def max_of_three(x,y,z):
    return max([x,y,z])

print(max_of_three(-1,5,3))

# Quersummenrechner
def Quersumme(num):
    return sum(i + 1 for i in range(num))

print(Quersumme(10))

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

