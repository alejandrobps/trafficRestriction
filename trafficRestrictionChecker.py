#!/usr/bin/python

### Traffic Restriction Predictor ###
### Author: Manuel Alejandro Beltran ###
### Date: Mar 6th, 2018 ###

## Libraries
import datetime
import time

## Classes
class licensePlate: #Customer's license plate
    def __init__(self, plateString):
        self.plateId = plateString
    
    def findLastDigit(self):
        return self.plateId[-1]
        
class trafficRestriction: #Restriction validator
    def __init__(self, lastDigit, ddt):
        self.digit = int(lastDigit)
        self.driveDateTime = ddt
        self.driveTime = datetime.timedelta(hours= int(ddt.timetuple()[3]), minutes= int(ddt.timetuple()[4]))
        self.dow = int(ddt.timetuple()[6])
        
    def trafficRestrictionDay(self): #checks if the day presents a restriction for the customer. This method returns 1 if there's a restriction, 0 when is allowed to drive on that day.
        if self.digit in range(1,3) and self.dow == 0:
            return 1
        elif self.digit in range(3,5) and self.dow == 1:
            return 1
        elif self.digit in range(5,7) and self.dow == 3:
            return 1
        elif self.digit in range(7,9) and self.dow == 4:
            return 1
        elif self.digit == 9 and self.dow == 5:
            return 1
        elif self.digit == 0 and self.dow == 5:
            return 1
        else:
            return 0

    def trafficRestrictionTime(self): #checks if the time presents a restriction for the customer. This method returns 1 if there's a restriction, 0 when is within the allowed time slots.
        if datetime.timedelta(hours=7, minutes=0) <= self.driveTime < datetime.timedelta(hours=9, minutes=30) or datetime.timedelta(hours=16, minutes=0) <= self.driveTime < datetime.timedelta(hours=19, minutes=30):
            return 1
        else:
            return 0

### Traffic Restriction Checker function
## checkTrafficRestriction(arg1_str, arg2_datetime): returns boolean 0 means allowed, 1 means restricted
def checkTrafficRestriction(licensePlateID, driveDateTime):
    
    ## Objects creation
    customerLP = licensePlate(licensePlateID)
    restrictionCheck = trafficRestriction(customerLP.findLastDigit(), driveDateTime)
    
    ## Core program, traffic restriction validation
    isRestrictedDay = restrictionCheck.trafficRestrictionDay()
    if isRestrictedDay == 1:
        isRestrictedTime = restrictionCheck.trafficRestrictionTime()
        if isRestrictedTime == 1:
            return 1
        else:
            return 0
    else:
        return 0    
### End of function