class Animal(object):
    def __init__(self, name, health=100):
        self.name = name
        self.health = 100
    def walk(self):
        self.health = self.health - 1
        return self
    def run(self):
        self.health = self.health - 5
        return self
    def displayHealth(self):
        print self.health

animal = Animal('Animal1')

animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__(self)
        self.health = 150
    def pet(self):
        self.health = self.health + 5
        return self

doggo = Dog()

doggo.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self):
        super(Dragon, self).__init__(self)
        self.health = 170
    def fly(self):
        self.health = self.health + 10
        return self
    def displayHealth(self):
        print "This is a dragon", self.health
        
drago = Dragon()

drago.walk().walk().walk().run().run().fly().fly().displayHealth()