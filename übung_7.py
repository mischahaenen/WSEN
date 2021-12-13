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
