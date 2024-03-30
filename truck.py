
class Truck:
    def __init__(self):
        self.miles = 0
        self.currentLocation = 0
        self.packages = []
        self.startingPoint = 0



    def __str__(self):
        return "%s, %s, %s" % (
            self.miles, self.currentLocation, self.packages)

