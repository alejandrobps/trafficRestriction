### Traffic Restriction Predictor ###
### Author: Manuel Alejandro Beltran ###
### Date: Mar 3rd, 2018 ###

## Libraries
import datetime
import time

## Global vars definition
looper = True

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
        self.driveDateTime = ddt
        self.driveTime = datetime.timedelta(hours= int(ddt.timetuple()[3]), minutes= int(ddt.timetuple()[4]))
        #print "\nTesting time aquired: ", self.driveTime
        self.dow = int(ddt.timetuple()[6])
        
    def trafficRestrictionDay(self):
        if self.digit in range(1,3) and self.dow == 0:
            print "Match 1 or 2"
            return 1
        elif self.digit in range(3,5) and self.dow == 1:
            print "Match 3 or 4"
            return 1
        elif self.digit in range(5,7) and self.dow == 3:
            print "Match 5 or 6"
            return 1
        elif self.digit in range(7,9) and self.dow == 4:
            print "Match 7 or 8"
            return 1
        elif self.digit == 9 and self.dow == 5:
            return 1
        elif self.digit == 0 and self.dow == 5:
            return 1
        else:
            print "Did not match"
            return 0

    def trafficRestrictionTime(self):
        if datetime.timedelta(hours=7, minutes=0) <= self.driveTime < datetime.timedelta(hours=9, minutes=30) or datetime.timedelta(hours=16, minutes=0) <= self.driveTime < datetime.timedelta(hours=19, minutes=30):
            return 1
        else:
            return 0

## Main program
while looper == True:
    print "TRAFFIC RESTRICTION PREDICTOR \nThis application will let you know if your car is allowed for circulation based on the License Plate and an specific date you are planning to drive \nLet's get started \n"
    licensePlateId = str(raw_input("Enter the license plate. I.e. ABC1234 : "))
    dateToDrive = str(raw_input("Enter the date you plan to drive. I.e. DD/MM/YYYY : "))
    timeToDrive = str(raw_input("Enter the time that you will start to drive. I.e. HH:MM : "))

    ## Parser 
    driveDateTime = datetime.datetime(int(dateToDrive[6:10]),int(dateToDrive[3:5]),int(dateToDrive[0:2]),int(timeToDrive[0:2]),int(timeToDrive[-2:]))
    
    ## End Parser
    
    print "Processing, please wait...\n"
    time.sleep(1)
    customerLP = licensePlate(licensePlateId)
    restrictionCheck = trafficRestriction(customerLP.findLastDigit(), driveDateTime)
    isRestrictedDay = restrictionCheck.trafficRestrictionDay()
    if isRestrictedDay == 1:
        isRestrictedTime = restrictionCheck.trafficRestrictionTime()
        if isRestrictedTime == 1:
            print "WARNING: Your car is restricted for circulation :(\n"
        else:
            print "OK: You can drive :)"
    else:
        print "OK: You can drive :)"
    print "\n\n\n"
    time.sleep(3)