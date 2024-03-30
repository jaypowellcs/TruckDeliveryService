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


# Load Truck 1 packages at 8:00 am - packages  1, 7, 8,  13, 14, 15, 19, 20, 21, 22, 23, 24, 29, 34
truck1packages = [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40]

# Load Truck 2 packages at 9:05 am - packages 3, 6, 10, 11, 12, 18, 25, 28, 30, 31, 32, 36, 38
truck2packages = [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39]

# Load Truck 3 packages can deliver EOD 2, 4, 5, 9, 17, 26, 27, 33, 35, 37, 39, 40
truck3packages = [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33]

# Creation of Trucks with starting time HH:MM:SS
truck1 = Truck('08:00:00')
truck2 = Truck('09:05:00')
truck3 = Truck('11:00:00')

def miles_to_time(distance_miles):
    average_speed_mph = 18
    # Calculate the time in hours
    time_hours = distance_miles / average_speed_mph

    # Convert hours to seconds
    time_seconds = int(time_hours * 3600)

    # Convert seconds to HH:mm:ss format
    hours, remainder = divmod(time_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def add_times(time1, time2):
    # Parse the input times
    hours1, minutes1, seconds1 = map(int, time1.split(":"))
    hours2, minutes2, seconds2 = map(int, time2.split(":"))

    # Calculate the total seconds
    total_seconds = (hours1 + hours2) * 3600 + (minutes1 + minutes2) * 60 + seconds1 + seconds2

    # Convert total seconds to HH:mm:ss format
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


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
        #Change all package status to 'En Route'
        Package.status = 'En Route'
        packageIndexes.append(find_index_2d(Package.address))

    #print(packageIndexes)
    #print(distances)
    #print(truck.packages)

    while len(packageIndexes) > 0:
        for i in packageIndexes:
            package_address = i  # Retrieve the package's address
            dist = distanceBetween(truck.currentLocation, package_address)  # Calculate distance
            distances.append(dist)  # Add distance to the list

        #print("222222")
        #print('Package Index', packageIndexes)
        #print('Distances', distances)
        #print('Actually Packages', truck.packages)

        #print('Distance 0', distances[0])
        #min_distance = distances[0]
        #print(min_distance)
        #or i in range(0, len(distances)):
            #print(distances[i])
            #if distances[i] <= min_distance:
                #min_distance = distances[i]
                #print(min_distance)

        #min distance of package from distance list
        min_distance = min(distances, key=float)
        #print('Min_Distance Found',min_distance)

        indexOfPackage = packageIndexes[distances.index(min_distance)]
        #print('Package Index',indexOfPackage )
        packageDelivered = truck.packages[packageIndexes.index(indexOfPackage)]
        #print('Package ID', packageDelivered)


        #Changing the status of a package from 'En Route' To delivered
        #print('Package Delivered:',packageHashTable.search(packageDelivered))
        Package = packageHashTable.search(packageDelivered)
        #print('Package this is',Package)

        #Updating the time of the program
        timeDelivered = miles_to_time(float(min_distance))
        deliveryTime = add_times(truck.time, timeDelivered)
        truck.time = deliveryTime
        #print(deliveryTime)
        Package.status = f'Delivered, {deliveryTime}'
        #print('Package Delivered:', packageHashTable.search(packageDelivered))

        #Find time package delivered
        #print("Time",miles_to_time(float(min_distance)))
        #Add min distance to total truck miles
        truck.miles += float(min_distance)
        #print('Truck Miles', min_distance)

        truck.currentLocation = indexOfPackage
        #print('New Truck Current Location', indexOfPackage)
        packageIndexes.remove( indexOfPackage)
        truck.packages.remove(packageDelivered)
        distances.clear()
        #print("333333")
        #print('Package Index', packageIndexes)
        #print('Distances', distances)
        #print('Actually Packages', truck.packages)

    #print('Total Truck Miles',truck.miles)
    #print("Truck 1 has delivered all their packages")

def hashTablePrint(packageHashTable):
    print("Packages:")
    # Fetch data from Hash Table
    for i in range(len(packageHashTable.table) + 1):
        print("Packages: {}".format(packageHashTable.search(i)))  # 1 to 11 is sent to myHash.search()

def hashTableSingleSearch(packageHashTable, packageID):
    return packageHashTable.search(packageID)


class Main:
    #User Interface
    while True:
        print("\nWelcome to the WGUPS package delivery program")
        print("Below are some options you can run during the program\n")
        print("***************************************")
        print("1. Print All Package Status and Total Mileage")
        print("2. Get a Single Package Status with a Time")
        print("3. Get All Package Status with a Time")
        print("4. Exit the Program")
        print("***************************************")

        # Get Input from user
        userInput = input("Type in start to begin the delivery proceess and you can press exit to stop the program at "
                          "anytime.\n")
        if userInput == 'start':
            deliverPackages(truck1)
            deliverPackages(truck2)
            deliverPackages(truck3)
            print(f"Total Miles Driven {truck1.miles + truck2.miles + truck3.miles} ")
        elif userInput == '1':
            hashTablePrint(packageHashTable)
        elif userInput == '2':
            userInput = input("Type in the package you want to search for.\n")
            print(hashTableSingleSearch(packageHashTable, int(userInput)))
        elif userInput == '3':
            hashTablePrint(packageHashTable)
        elif userInput == '4':
            print("Exiting...")
            break
        else:
            print('Unknown Error')


