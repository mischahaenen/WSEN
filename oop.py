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

''' 
Dataclasses are python classes but are suited for storing data objects.
This module provides a decorator and functions for automatically adding generated special methods
such as __init__() and __repr__() to user-defined classes.
'''

@dataclass
class Product:
    name: str
    count: int = 0
    price: float = 0.0
    
    def betrag(self): return self.count * self.price
''' 
Features
1.  They store data and represent a certain data type.
    Ex: A number. For people familiar with ORMs, a model instance is a data object. It represents a specific kind of entity.
2.  It holds attributes that define or represent the entity. They can be compared to other objects of the same type.
    Ex: A number can be greater than, less than, or equal to another number.
'''
product = Product('Python', 1, 2)
product2 = Product('Python', 1, 2)
print(product.count)
print(product == product2)
print(product.betrag())

# ENUM
from enum import IntEnum
class author(IntEnum):
    VALUE1 = 1
    VALUE2 = 2
    VALUE3 = 3
print(author.VALUE1 == 1)

class Dog:
    # Class attribute
    species = "Canis familiaris"
    def __init__(self, name, age):
        #Instance attributes
        self.name = name
        self.age = age
        
    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old'
        
    def bark(self) -> str:
        return 'woof!'
    
    def description(self) -> str:
        return f'{self.name} is {self.age} years old'

       
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)


print(buddy.age)
print(miles.bark())
print(miles)


