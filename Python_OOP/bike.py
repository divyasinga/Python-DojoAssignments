class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        print 'New bike!'
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayinfo(self):
        print self.price, self.max_speed, self.miles
    def riding(self):
        print 'Riding...'
        self.miles = self.miles + 10
        print self.miles
        return self
    def reversing(self):
        print 'Reversing..'
        self.miles = self.miles - 5
        print self.miles
        return self

schwinn = Bike(300, '25mph')
meka = Bike(900000, '50mph')
epona = Bike(1000, '40mph')

schwinn.riding().riding().riding().displayinfo()

meka.riding().riding().reversing().reversing().displayinfo()

epona.reversing().reversing().reversing().displayinfo()