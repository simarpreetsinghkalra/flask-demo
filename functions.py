from dimensions import Dimensions
from calculatedValues import CalculatedValues

def doCalculate(dimensionsFromApi):
    # creating object of class Dimensions
    dimensions = Dimensions(dimensionsFromApi)
    print('Dimensions: ', dimensions.getDimensions()) # using member function of Dimensions class to get all dimensions
    
    # creating object of class CalculatedValues
    calculatedValues = CalculatedValues()
    
    calculatedValues.calculatePerimeter(dimensions)
    calculatedValues.calculateArea(dimensions)
    calculatedValues.calculateVolume(dimensions)
    calculatedValues.calculateLaSurfaceArea(dimensions)
    
    print('Perimeter: ', calculatedValues.getPerimeter())
     
    return calculatedValues.createResponse()