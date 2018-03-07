import unittest
import datetime
import trafficRestrictionChecker
from trafficRestrictionChecker import licensePlate

# Class Testing definition
class testTrafficRestriction(unittest.TestCase):
    
    def test_checkTrafficRestriction(self):
        
        #Scenario 1: All cars are allowed on weekend
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("ABC0001", datetime.datetime(int(2017),int(12),int(31),int(8),int(30))), 0)
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("ABC9999", datetime.datetime(int(2018),int(3),int(3),int(17),int(40))), 0)

        #Scenario 2: All cars are allowed to drive from 00h00 to 06h59
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("AEI1234", datetime.datetime(int(2018),int(3),int(6),int(0),int(0))), 0)
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("AEI1234", datetime.datetime(int(2018),int(3),int(6),int(6),int(59))), 0)
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("AEI6666", datetime.datetime(int(2018),int(3),int(6),int(4),int(30))), 0)
        
        #Scenario 3: All cars are allowed to drive from 09h31 to 15h59
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("IOU1010", datetime.datetime(int(2018),int(3),int(9),int(9),int(31))), 0)
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("IOU1011", datetime.datetime(int(2018),int(3),int(9),int(15),int(59))), 0)
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("IOU1012", datetime.datetime(int(2018),int(3),int(9),int(13),int(25))), 0)
        
        #Scenario 4: All cars are allowed to drive from 19h31 to 23h59
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("PPI3141", datetime.datetime(int(2024),int(4),int(8),int(19),int(31))), 0)
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("PPI3141", datetime.datetime(int(2024),int(4),int(8),int(23),int(59))), 0)
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("PPI1777", datetime.datetime(int(2024),int(4),int(8),int(21),int(4))), 0)
        
        #Scenario 5: Cars with license plate 1 or 2 are restricted to drive from 07h00 to 09h30 on Mondays, the rest of cars can circulate normal.
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("RES4321", datetime.datetime(int(2018),int(3),int(5),int(7),int(10))), 1)
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("RES4321", datetime.datetime(int(2003),int(4),int(7),int(8),int(59))), 1)
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("RES4321", datetime.datetime(int(2048),int(4),int(6),int(9),int(0))), 1)
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("RES4444", datetime.datetime(int(2020),int(11),int(30),int(7),int(1))), 0)
        
        #Scenario 6: Cars with license plate 3 or 4 are restricted to drive from 16h00 to 19h30 on Tuesdays, the rest of cars can circulate normal.
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("UIO0003", datetime.datetime(int(2018),int(3),int(6),int(16),int(0))), 1)
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("UIO3344", datetime.datetime(int(2018),int(3),int(13),int(18),int(0))), 1)
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("ABC1235", datetime.datetime(int(2018),int(3),int(6),int(16),int(50))), 0)
        
        #Scenario 7: Cars with license plate 5 or 6 are not allowed to drive on Restriction periods on Wednesdays, the rest of cars can circulate normal.
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("UIO0005", datetime.datetime(int(2018),int(2),int(28),int(7),int(0))), 1)
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("UIO3366", datetime.datetime(int(2016),int(2),int(10),int(18),int(0))), 1)
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("ABC1111", datetime.datetime(int(2018),int(2),int(28),int(16),int(50))), 0)
        
        #Scenario 9: Cars with license plate 7 or 8 are not allowed to drive on Restriction periods on Thursday, the rest of cars can circulate normal.
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("FOO0987", datetime.datetime(int(2018),int(3),int(8),int(9),int(29))), 1)
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("BAR0098", datetime.datetime(int(2046),int(4),int(5),int(19),int(21))), 1)
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("DOE1100", datetime.datetime(int(2018),int(1),int(4),int(7),int(15))), 0)
        
        #Scenario 9: Cars with license plate 9 or 0 are not allowed to drive on Restriction periods on Friday, the rest of cars can circulate normal.
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("JON9190", datetime.datetime(int(2018),int(3),int(9),int(7),int(0))), 1)
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("QWE1000", datetime.datetime(int(2000),int(4),int(7),int(16),int(0))), 1)
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("ASD0101", datetime.datetime(int(2000),int(4),int(7),int(16),int(0))), 0)
        
        
    def test_checkLastDigit(self):
        
        #Check Lastdigit of a License Plate
        driver1Plate = licensePlate("ABC1234")
        driver2Plate = licensePlate("XYZ9876")
        self.assertEquals(driver1Plate.findLastDigit(),4)
        self.assertEquals(driver2Plate.findLastDigit(),6)
        
        
if __name__ == "__main__":
    unittest.main()