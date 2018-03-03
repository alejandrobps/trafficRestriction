### Traffic Restriction Predictor ###
### Author: Manuel Alejandro Beltran ###

## Libraries

## Global vars definition

## Global functions

## Global classes
class licensePlate:
    def __init__(self, plateString):
        self.plateId = plateString
        self.lastDigit = findLastDigit(self.plateId)
        
    def findLastDigit(self):
        self.lastDigit = self.plateId[-1]

## Main program