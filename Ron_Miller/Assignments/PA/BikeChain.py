import time

class Bike(object):
    
    def __init__(self,price,max_speed,miles=0):
        self.price=price
        self.max_speed=max_speed
        self.miles=miles
        

    def getInfo(self):
        print "Price: " + str(self.price) + "\nMaximum speed: "+ str(self.max_speed) +"\nMiles: "+ str(self.miles)
        return self
    
    def ride(self):
        print "riding...."
        time.sleep(2)
        self.miles + = 10
        return self

    def reverse(self):
        print "reversing...."
        time.sleep(2)
        self.miles-=10
        return self 

T = Bike(1000,200)
F = Bike(10,2000)
O = Bike(100,20000)

T.ride().ride().ride().reverse().getInfo()


