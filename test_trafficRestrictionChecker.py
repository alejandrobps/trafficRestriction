import unittest
import datetime
import trafficRestrictionChecker

print "Restricted: ", trafficRestrictionChecker.checkTrafficRestriction("ABC1001", datetime.datetime(int(2018),int(3),int(5),int(7),int(10)))
print "Ok fine: ", trafficRestrictionChecker.checkTrafficRestriction("PBC9999", datetime.datetime(int(2018),int(3),int(3),int(17),int(40)))
# Class definition
class testTrafficRestriction(unittest.TestCase):
    def test_checkTrafficRestriction(self):
        
        #Scenario 1: All cars are allowed on weekend
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("ABC0001", datetime.datetime(int(2018),int(3),int(3),int(10),int(10))), 0)
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("PBC9999", datetime.datetime(int(2018),int(3),int(3),int(17),int(40))), 1)

        #Scenario 2: All cars are allowed to drive from 00h00 to 06h59
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("ABC1234", datetime.datetime(int(2018),int(3),int(6),int(12),int(0))), 0)
        
        #Scenario 3: All cars are allowed to drive from 09h31 to 15h59
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("ABC1234", datetime.datetime(int(2018),int(3),int(6),int(12),int(0))), 0)
        
        #Scenario 4: All cars are allowed to drive from 19h31 to 23h59
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("ABC1234", datetime.datetime(int(2018),int(3),int(6),int(12),int(0))), 0)
        
        #Scenario 5: Cars with license plate 1 or 2 are allowed to drive on Monday, in a non-restricted period
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("ABC1234", datetime.datetime(int(2018),int(3),int(6),int(12),int(0))), 0)
        
        #Scenario 6: Cars with license plate 1 or 2 are restricted to drive from 07h00 to 09h30 
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("ABC1001", datetime.datetime(int(2018),int(3),int(5),int(7),int(10))), 1)
        
        #Scenario 7: Cars with license plate 1 or 2 are restricted to drive from 16h00 to 19h30 
        self.assertEquals(trafficRestrictionChecker.checkTrafficRestriction("ABC1234", datetime.datetime(int(2018),int(3),int(6),int(12),int(0))), 0)
        
        
if __name__ == "__main__":
    unittest.main()