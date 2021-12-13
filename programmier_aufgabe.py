from typing import List

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
        for index in range(0, self.dimension):
            non_zero_value = self.getNonzeroValueByIndex(index)
            if (non_zero_value is not None):
                vector.append(non_zero_value)
            else:
                vector.append(0)
        return vector 
    # überprüft, ob index i kleiner als dimension und positiv ist, dann Vektorelement mit index i, diesen Wert(value) erhalten
    def getNonzeroValueByIndex(self, index: int):
        if (self.dimension < index or index < 0):
            return None
        if (index in self.nonzeroIndexes):
            i = self.nonzeroIndexes.index(index)
            return self.nonzeroValues[i]
        else:
            return None
    # multipliziert den Vektor mit einem factor
    def multiply(self, factor: float):
        multiplied_vector = []
        for value in self.nonzeroValues:
            multiplied_vector.append(value * factor)
        return multiplied_vector
       
    # welche aus den zwei Sparse-Vektoren a und b die Summe bildet und diesen als neues Sparse-Objekt zurückgibt.
    def addSparse(self, vector: object) -> object:
        summed_vector = list(map(lambda x, y: x + y, self.getVectorWithZeroValues(), vector.getVectorWithZeroValues()))
        non_zero_indexes = []
        non_zero_values = []
        for index, value in enumerate(summed_vector):
            if (value is not 0):
                non_zero_indexes.append(index)
                non_zero_values.append(value)
                
        return SparseVector(len(summed_vector), non_zero_values, non_zero_indexes)
            
    # welche das Skalarprodukt der beiden Sparse-Vektoren berechnet und zurückgibt.
    def dotSparse(self, vector: object):
        print(vector)
        
    # die ein Objekt der Klasse SparseVektor mit den folgenden Eigenschaften erzeugt
    def createRandomSparse(n,m,a,b):
        print(n)
        
sparse1 = SparseVector(11, [1,2,3,4], [2,3,4,5])
sparse2 = SparseVector(10, [1,5,6,8], [0,1,4,9])
# Tests
print(sparse1)
print(sparse1.getDimension())
print(sparse1.getNonzeroIndexes())
print(sparse1.getNonzeroValues())
print(sparse1.getNonzeroValueByIndex(-2))
print(sparse1.getNonzeroValueByIndex(2))
print(sparse1.multiply(3))
print(sparse1.addSparse(sparse2))
