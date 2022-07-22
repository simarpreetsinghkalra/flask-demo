# importing all calculation helper functions from respective calculation packages
from calculations.perimeter import calculatePerimeter
from calculations.area import calculateArea
from calculations.volume import calculateVolume
from calculations.laSurfaceArea import calculateLateralSurfaceArea

# creating a class to store all calculated values
class CalculatedValues:
    perimeter = 0
    area = 0
    volume = 0
    laSurfaceArea = 0

    # defining member functions to get and set all calculated values
    # these methords are called getters and setters
    
    def setPerimeter(self, perimeter):
        self.perimeter = perimeter
    
    def getPerimeter(self):
        return self.perimeter
    
    def setArea(self, area):
        self.area = area
        
    def getArea(self):
        return self.area
    
    def setVolume(self, volume):
        self.volume = volume
    
    def getVolume(self):
        return self.volume
    
    def setLaSurfaceArea(self, laSurfaceArea):
        self.laSurfaceArea = laSurfaceArea
    
    def getLaSurfaceArea(self):
        return self.laSurfaceArea
    
    # defining member function to calculate all required values, storing them in class attributes and at last returning them using getters
    def calculatePerimeter(self, dimensions):
        perimeter = calculatePerimeter(dimensions.getDimensions())
        self.setPerimeter(perimeter)
        return self.getPerimeter()

    def calculateArea(self, dimensions):
        area = calculateArea(dimensions.getDimensions())
        self.setArea(area)
        return self.getArea()

    def calculateVolume(self, dimensions):
        volume = calculateVolume(dimensions.getDimensions())
        self.setVolume(volume)
        return self.getVolume()
    
    def calculateLaSurfaceArea(self, dimensions):
        laSurfaceArea = calculateLateralSurfaceArea(self.getPerimeter(), dimensions.getDimensions()) # example of passing precalculated value to new calculation
        self.setLaSurfaceArea(laSurfaceArea)
        return self.getLaSurfaceArea()
    
    # defining member function to create response from all calculated values
    def createResponse(self):
        return {
            "primeter": self.getPerimeter(),
            "area": self.getArea(),
            "volume": self.getVolume(),
            "laSurfaceArea": self.getLaSurfaceArea()
        }