#!/usr/bin/python

### Traffic Restriction Predictor ###
### Author: Manuel Alejandro Beltran ###
### Date: Mar 3rd, 2018 ###
# The "Pico y Placa" is a traffic restriction system that operates in the city of Quito. It restricts cars from circulation depending on the last digit of the license plate in an specific day of the week from the time slots 7:00 to 9:30 and 16:00 to 19:30. On Monday the cars terminating their license plate on 1 & 2 are restricted, Tuesday for 3 & 4, Wednesday 5 & 6, Thursday 7 & 8 and Friday 9 & 0. Weekends all cars are allowed to transit.

## Libraries
import datetime
import time
import trafficRestrictionChecker

## Global vars
looper = True
looperval = 0

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
                print "Wrong entry, the format used should be ABC1234"
        else:
            print "Wrong entry, the format used should be ABC1234"
   
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
            
    driveDateTime = datetime.datetime(int(dateToDrive[6:10]),int(dateToDrive[3:5]),int(dateToDrive[0:2]),int(timeToDrive[0:2]),int(timeToDrive[-2:]))
    print "Processing, please wait...\n\n"
    time.sleep(1)
    print "The car with license plate:", licensePlateId, ", planning to drive on:", driveDateTime
    drivingAllowed = trafficRestrictionChecker.checkTrafficRestriction(licensePlateId, driveDateTime)
    if drivingAllowed == 0:
        print "RESULT:\tOK! Your car is allowed to drive ;)\n\n\n"
    else:
        print "RESULT:\tWARNING! Your car is restricted for circulation :(\n\n\n"        
    time.sleep(3)
    
    ## Carry on looper
    looperval = raw_input("Do you wish to continue checking? [yes/no] ")
    if len(looperval) != 0:
        if str(looperval) == "no" or str(looperval) == "n" or str(looperval) == "No" or str(looperval) == "NO" or str(looperval) == "N" or str(looperval) == "nO":
            print "\n\n\nGoodbye!\n\n"
            break
    else:
        looperval = "carryon"
    time.sleep(1)
    print "\n\n\n\n"
    
### End of the program