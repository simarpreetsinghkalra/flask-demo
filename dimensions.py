# defining dimensionns class

class Dimensions:
    # these are attributes of class Dimensions
    l = 0
    b = 0
    h = 0
    
    # this is a construcctor of class Dimensions
    def __init__(self, dimensions):
        self.l = dimensions['l']
        self.b = dimensions['b']
        self.h = dimensions['h']
    
    # member function to get all dimensions
    def getDimensions(self):
        return {'l': self.l, 'b': self.b, 'h': self.h }
