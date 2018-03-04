### Traffic Restriction Predictor ###
### Author: Manuel Alejandro Beltran ###
### Date: Mar 3rd, 2018 ###

## Libraries
import datetime

## Global vars definition
weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday"] 
licensePlateId = "None"

## Global functions
        
## Global classes
class licensePlate:
    def __init__(self, plateString):
        self.plateId = plateString
    def findLastDigit(self):
        return self.plateId[-1]
        
class trafficRestriction:
    def __init__(self, lastDigit, ddt):
        self.digit = int(lastDigit)
        self.dow = int(ddt.timetuple()[6])
        
    def trafficRestrictionDay(self):
        print "Control:", self.digit, self.dow
        if self.digit in range(1,3) and self.dow == 0:
            print "Match 1 or 2"
            return 1
            #self.allowanceBoolean = 1 #1 is restricted, 0 is allowed to be driven
        elif self.digit in range(3,5) and self.dow == 1:
            print "Match 3 or 4"
            return 1
            #self.allowanceBoolean = 1 #1 is restricted, 0 is allowed to be driven
        elif self.digit in range(5,7) and self.dow == 3:
            print "Match 5 or 6"
            return 1
            #self.allowanceBoolean = 1 #1 is restricted, 0 is allowed to be driven
        elif self.digit in range(7,9) and self.dow == 4:
            print "Match 7 or 8"
            return 1
            #self.allowanceBoolean = 1 #1 is restricted, 0 is allowed to be driven
        elif self.digit == 9 and self.dow == 5:
            return 1
            #self.allowanceBoolean = 1 #1 is restricted, 0 is allowed to be driven
        elif self.digit == 0 and self.dow == 5:
            return 1
            #self.allowanceBoolean = 1 #1 is restricted, 0 is allowed to be driven
        else:
            print "Did not match"
            return 0
            #self.allowanceBoolean = 0
    def trafficRestrictionTime(self):
        return 0
    
    
## Main program
print "TRAFFIC RESTRICTION PREDICTOR \nThis application will let you know if your car is allowed for circulation based on the License Plate and an specific date you are planning to drive \nLet's get started ;)\n\n"
licensePlateId = str(raw_input("Enter the license plate. I.e. ABC1234 : "))
dateToDrive = str(raw_input("Enter the date you plan to drive. I.e. DD/MM/YYYY : "))
timeToDrive = str(raw_input("Enter the time that you will start to drive. I.e. HH:MM : "))

##PARSER HERE##
dayOnly = int(dateToDrive[0:2])
monthOnly = int(dateToDrive[3:5])
yearOnly = int(dateToDrive[6:10])
hourOnly = int(timeToDrive[0:2])
minuteOnly = int(timeToDrive[-2:])
driveDateTime = datetime.datetime(yearOnly,monthOnly,dayOnly,hourOnly,minuteOnly)
print "TIME CHECK:", driveDateTime.timetuple(), "DotW", driveDateTime.timetuple()[6]
## ##

print "In summary for:"
print licensePlateId
print dateToDrive
print timeToDrive

customerLP = licensePlate(licensePlateId)
print "Here the last digit", customerLP.findLastDigit()
#print customerLP.findLastDigit()
print dateToDrive
restrictionCheck = trafficRestriction(customerLP.findLastDigit(), driveDateTime)
isRestrictedDay = restrictionCheck.trafficRestrictionDay()