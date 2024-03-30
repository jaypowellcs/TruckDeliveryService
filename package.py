import csv

import package
from hashtable import HashTable


# Create class for packages called package
class Package:
    def __init__(self, packageID, address, city, state, Zip, deadline, weight, special, status):
        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.Zip = Zip
        self.deadline = deadline
        self.weight = weight
        self.special = special
        self.status = status

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s," % (
            self.packageID, self.address, self.city, self.state, self.Zip, self.deadline,
            self.weight, self.special, self.status)


def loadPackageData(fileName):
    with open(fileName) as packagesList:
        packageData = csv.reader(packagesList, delimiter=',')
        next(packageData)  # skip header
        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = package[4]
            pDeadline = package[5]
            pWeight = package[6]
            pSpecial = package[7]
            pStatus = "Loaded"

            # package object
            package = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pWeight, pSpecial, pStatus)

            packageHashTable.insert(pID, package)


packageHashTable = HashTable()

loadPackageData('packages.csv')

