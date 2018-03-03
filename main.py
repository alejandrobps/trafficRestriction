### Traffic Restriction Predictor ###
### Author: Manuel Alejandro Beltran ###
### Date: Mar 3rd, 2018 ###

## Libraries

## Global vars definition

## Global functions
def trafficRestriction(licensePlateId, dayOfTheWeek):
    if licensePlateId.lastDigit in range(1,3) and dayOfTheWeek == "Monday":
        allowanceBoolean = 1 #1 is restricted, 0 is allowed to be driven
    elif licensePlateId.lastDigit in range(3,5) and dayOfTheWeek == "Tuesday":
        allowanceBoolean = 1 #1 is restricted, 0 is allowed to be driven
    elif licensePlateId.lastDigit in range(5,7) and dayOfTheWeek == "Wednesday":
        allowanceBoolean = 1 #1 is restricted, 0 is allowed to be driven
    elif licensePlateId.lastDigit in range(7,9) and dayOfTheWeek == "Thursday":
        allowanceBoolean = 1 #1 is restricted, 0 is allowed to be driven
    elif licensePlateId.lastDigit == 9 and dayOfTheWeek == "Friday":
        allowanceBoolean = 1 #1 is restricted, 0 is allowed to be driven
    elif licensePlateId.lastDigit == 0 and dayOfTheWeek == "Friday":
        allowanceBoolean = 1 #1 is restricted, 0 is allowed to be driven
    else:
        allowanceBoolean = 0
        
## Global classes
class licensePlate:
    def __init__(self, plateString):
        self.plateId = plateString
        self.lastDigit = findLastDigit(self.plateId)
        
    def findLastDigit(self):
        self.lastDigit = self.plateId[-1]
    
## Main program