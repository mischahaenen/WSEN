def isPrimeNumber(num):
    if num <=1: return False;
    for i in range(2,num):
        if (num % i) == 0: return False;
    return True

for i in range(100):
    print(i, 'ist eine Primzahl'if isPrimeNumber(i) == True else 'ist keine Primzahl' )
        