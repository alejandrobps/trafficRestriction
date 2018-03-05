#!/usr/bin/python

### Traffic Restriction Predictor ###
### Author: Manuel Alejandro Beltran ###
### Date: Mar 3rd, 2018 ###
# The "Pico y Placa" is a traffic restriction system that operates in the city of Quito. It restricts cars from circulation depending on the last digit of the license plate in an specific day of the week from the time slots 7:00 to 9:30 and 16:00 to 19:30. On Monday the cars terminating their license plate on 1 & 2 are restricted, Tuesday for 3 & 4, Wednesday 5 & 6, Thursday 7 & 8 and Friday 9 & 0. Weekends all cars are allowed to transit.

## Libraries
import datetime
import time
import unittest

## Global vars
looper = True
looperval = 0

## Global functions
        
## Global classes
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

## Main program
while looper == True:
    print "\nTRAFFIC RESTRICTION PREDICTOR \nThis application will let you know if your car is allowed for circulation based on the License Plate and an specific date you are planning to drive \nLet's get started \n"
    
    ## Input checker
    while True:
        licensePlateId = str(raw_input("Enter the license plate. I.e. ABC1234 : "))
        if len(licensePlateId) == 7:
            if licensePlateId[3:].isdigit() and not licensePlateId[0].isdigit() and not licensePlateId[1].isdigit() and not licensePlateId[2].isdigit(): # Not validated for special characters, though. Next phase will support this feature.
                break
            else:
                print "Wrong entry, the format used should be AAA1234"
        else:
            print "Wrong entry, the format used should be AAA1234"
   
    while True:
        dateToDrive = str(raw_input("Enter the date you plan to drive. I.e. DD/MM/YYYY : "))
        if len(dateToDrive) == 10:
            #print "Checking time: ",dateToDrive[0:2],dateToDrive[3:5],dateToDrive[6:10]
            if dateToDrive[0:2].isdigit() and dateToDrive[3:5].isdigit() and dateToDrive[6:10].isdigit():
                if 0 < int(dateToDrive[0:2]) <= 31 and 0 < int(dateToDrive[3:5]) <= 12 and 2000 < int(dateToDrive[6:10]) < 2050:
                    break
                else:
                    print "Wrong entry, the format used should be DD/MM/YYYY. Date must be between 1999 to 2050"
            else:
                print "Wrong entry, the format used should be DD/MM/YYYY. Date must be between 1999 to 2050"
        else:
            print "Wrong entry, the format used should be DD/MM/YYYY. Date must be between 1999 to 2050"
            
    while True:
        timeToDrive = str(raw_input("Enter the time that you will start to drive. I.e. HH:MM : "))
        if len(timeToDrive) == 5:
            #print "Checking time: ",timeToDrive[0:2],timeToDrive[3:5]
            if timeToDrive[0:2].isdigit() and timeToDrive[3:5].isdigit():
                if 0 < int(timeToDrive[0:2]) <= 23 and 0 <= int(timeToDrive[3:5]) <= 59:
                    break
                else:
                    print "Wrong entry, the format used should be HH:MM."
            else:
                print "Wrong entry, the format used should be HH:MM."
        else:
            print "Wrong entry, the format used should be HH:MM."
            
    ## Populate variables
    driveDateTime = datetime.datetime(int(dateToDrive[6:10]),int(dateToDrive[3:5]),int(dateToDrive[0:2]),int(timeToDrive[0:2]),int(timeToDrive[-2:]))
    
    print "Processing, please wait...\n"
    time.sleep(2)
    
    ## Objects creation
    customerLP = licensePlate(licensePlateId)
    restrictionCheck = trafficRestriction(customerLP.findLastDigit(), driveDateTime)
    
    ## Core program, traffic restriction validation
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
    
    ## Carry on looper
    print "Further options\nIf you wish to continue checking, enter yes or any key.\n"
    looperval = raw_input("Do you wish to continue? [yes/no] ")
    if len(looperval) != 0:
        if str(looperval) == "no" or str(looperval) == "n" or str(looperval) == "No" or str(looperval) == "NO" or str(looperval) == "N" or str(looperval) == "nO":
            print "\n\n\nGoodbye!\n\n"
            break
    else:
        looperval = "carryon"
    time.sleep(1)
    print "\n\n\n\n"
    
    ### End of the program