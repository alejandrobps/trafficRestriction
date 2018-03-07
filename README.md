# trafficRestriction
The "Pico y Placa" is a traffic restriction system that operates in the city of Quito. It restricts cars from circulation depending on the last digit of the license plate, in an specific day of the week from the time slots 7:00 to 9:30 and 16:00 to 19:30. On Monday the cars terminating their license plate on 1 & 2 are restricted, Tuesday 3 & 4, Wednesday 5 & 6, Thursday 7 & 8 and Friday 9 & 0. Weekends all cars are allowed to transit.

This program let you to check whether your car is allowed to be driven or not within the Restriction Periods on weekdays.
Just enter the license plate code, which is structured by three letters followed by four numbers, I.e, ABC1234. Then just insert the date in Ecuadorian format DD/MM/YYYY, and the time that the car is circulating.

The code was made on python 2.7.
The program contains a main module main.py, which contains the structure of execution of the program.
The core traffic restriction checker classes and methods are located in the trafficRestrictionChecker.py.
Finally there is a unit test module test_trafficRestrictionChecker.py analyzing several scenarios.

To Execute the program:
  python main.py
 
To Execute unit testing:
  python test_trafficRestrictionChecker.py