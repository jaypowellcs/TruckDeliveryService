# James Powell
# Student ID: 011190422
# C950

import csv

import package
from truck import Truck
import csv
import package
from hashtable import HashTable
from package import loadPackageData
from package import packageHashTable

# Start of program
# Read the file of distance information
with open("distance.csv") as csvfile:
    CSV_Distance = csv.reader(csvfile)
    CSV_Distance = list(CSV_Distance)

# Read the file of address information
with open("AddressFile.csv") as csvfile1:
    CSV_Address = csv.reader(csvfile1)
    CSV_Address = list(CSV_Address)


def distanceBetween(address1, address2):
    distance = CSV_Distance[address1][address2]
    return distance


def find_index_2d(element):
    for i, sublist in enumerate(CSV_Address):
        if element in sublist:
            return i
    return -1


# Load Truck 1 packages at 8:00 am - packages  7, 8, 13, 14, 15, 19, 20, 21, 22, 23, 24, 29, 34
truck1packages = [1, 7, 8,  13, 14, 15, 19, 20, 21, 22, 23, 24, 29, 34]

# Load Truck 2 packages at 9:05 am - packages
truck2packages = [3, 6, 10, 11, 12, 18, 25, 28, 30, 31, 32, 36, 38]

# Load Truck 3 packages can deliver EOD
truck3packages = [2, 4, 5, 9, 17, 26, 27, 33, 35, 37, 39, 40]

# Creation of Trucks
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

# Load Packages for Truck1
truck1.packages = truck1packages
truck2.packages = truck2packages
truck3.packages = truck3packages


def deliverPackages(truck):
    # list of package addresses
    packageIndexes = []
    # list of distances
    distances = []
    # For each package find the package address and match it to an address number
    for pID in truck.packages:
        Package = packageHashTable.search(pID)
        packageIndexes.append(find_index_2d(Package.address))

    while len(packageIndexes) > 1:
        for i in packageIndexes:
            package_address = i  # Retrieve the package's address
            dist = distanceBetween(truck.currentLocation, package_address)  # Calculate distance
            distances.append(dist)  # Add distance to the list

        min_distance = distances[0]
        for i in range(1, len(distances)):
            if distances[i] < min_distance:
                min_ele = distances[i]

        theLocation = packageIndexes[distances.index(min_distance)]
        packageDelivered = truck.packages[packageIndexes.index(theLocation)]

        truck.miles += float(min_distance)
        truck.startingPoint = theLocation
        packageIndexes.remove(theLocation)
        truck.packages.remove(packageDelivered)

    print(truck.miles)


deliverPackages(truck1)
deliverPackages(truck2)
deliverPackages(truck3)