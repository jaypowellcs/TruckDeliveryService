
class Truck:
    def __init__(self, depart_time):
        self.miles = 0
        self.currentLocation = 0
        self.packages = []
        self.startingPoint = 0
        self.depart_time = depart_time
        self.time = depart_time


    def __str__(self):
        return "%s, %s, %s" % (
            self.miles, self.currentLocation, self.packages)

