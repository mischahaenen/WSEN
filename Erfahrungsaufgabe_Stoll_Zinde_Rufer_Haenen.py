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



sparse1 = SparseVector(10, [1,2,3,4], [2,3,4,5])
sparse2 = SparseVector(10, [3,5,6,8], [1,2,4,9])
# Tests
print('-----------------------')
print('Sparse1')
print('-----------------------')
print(sparse1)
print('Dimension: ', sparse1.getDimension())
print('Non-Zero-Indexes: ', sparse1.getNonzeroIndexes())
print('Non-Zero-Values', sparse1.getNonzeroValues())
print('Value wenn Index 6 existiert : ', sparse1.getNonzeroValueByIndex(6))
print('Multipliziert Sparse1', sparse1.multiply(3))
print('-----------------------')
print('Sparse2')
print('-----------------------')
print(sparse2)
print('Dimension: ', sparse2.getDimension())
print('Non-Zero-Indexes: ', sparse2.getNonzeroIndexes())
print('Non-Zero-Values', sparse2.getNonzeroValues())
print('Value wenn Index 4 existiert : ', sparse2.getNonzeroValueByIndex(4))
print('Multipliziert Sparse2', sparse2.multiply(9))
print('-----------------------')
print('Berechnungen Sparse 1 & Sparse 2')
print('-----------------------')
print('Summe Sparse 1 & 2:')
print(addSparse(sparse1, sparse2))
print('Skalarprodukt Spare 1 & 2:', dotSparse(sparse1, sparse2))
print('Random Sparse n=10, m=5, a=1, b=6:')
print(createRandomSparse(10, 5, 1, 6))
