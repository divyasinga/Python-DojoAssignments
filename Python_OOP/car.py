class Car(object):
    def __init__(self, price, speed, fuel, mileage, tax=0.12):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def display_all(self):
        print 'Price:', self.price
        print 'Speed:', self.speed
        print 'Fuel:', self.fuel
        print 'Mileage:', self.mileage
        print 'Tax:', self.tax

Tesla = Car(35000, '90mph', 'Full', 'n/a')
Toyota = Car(9000, '70mph', 'Empty', '20mpg')
Honda = Car(20000, '80mph', 'Full', '35mpg')
Acura = Car(40000, '80mph', 'Full', '15mpg')
smart = Car(10000, '60mph', 'Full', '45mpg')

Tesla.display_all()
Toyota.display_all()
Honda.display_all()
Acura.display_all()
smart.display_all()