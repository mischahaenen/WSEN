def isPrimeNumber(num):
    if num <=1: return False;
    for i in range(2,num):
        if (num % i) == 0: return False;
    return True

for i in range(100):
    print(i, 'ist eine Primzahl'if isPrimeNumber(i) == True else 'ist keine Primzahl' )
        

import random
# initializes random generator
random.seed()
# prints a random value from the list
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))
print(random.random())
print(random.random())
print(random.randint(1, 15))
# Returns none
random.shuffle(list1)
print(list1)

