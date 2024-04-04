# James Powell
# Student ID: 011190422
# C950 WGUPS
from typing import List, Any

from hashtable import HashTable
from truck import Truck
import csv
from package import packageHashTable, loadPackageData

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


# Load Truck 1 packages at 8:00 am - packages  1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40,
truck1packages = [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40, ]

# Load Truck 2 packages at 9:05 am - packages 3, 6, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38,  25
truck2packages = [3, 6, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 25]

# discovered at 10:20 am that package #9 has the wrong address - needs changed to 410 S. State St., Salt Lake City,
# UT 84111 package9 = packageHashTable.search(9) package9.address = '410 S. State St.' package9.zip = '48111' Load
# Truck 3 packages can deliver EOD 2, 4, 5, 7, 8, 9, 10, 11, 28, 32, 33, 39, 12
truck3packages = [2, 4, 5, 7, 8, 9, 10, 11, 28, 32, 33, 39, 12]

# Creation of Trucks with starting time HH:MM:SSs
truck1 = Truck('08:00:00')
truck2 = Truck('09:05:00')
truck3 = Truck('12:03:00')


# convert the distances to miles to time
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


# add times to all the packages
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


# Deliver function of the packages
def deliverPackages(truck):
    # list of package addresses
    packageIndexes = []
    # list of distances
    distances = []
    # For each package find the package address and match it to an address number
    for pID in truck.packages:
        Package = packageHashTable.search(pID)
        # Change all package status to 'En Route'
        Package.status = 'En Route'
        packageIndexes.append(find_index_2d(Package.address))

    # print(packageIndexes)
    # print(distances)
    # print(truck.packages)

    while len(packageIndexes) > 0:
        for i in packageIndexes:
            package_address = i  # Retrieve the package's address
            dist = distanceBetween(truck.currentLocation, package_address)  # Calculate distance
            distances.append(dist)  # Add distance to the list

        # print("222222")
        # print('Package Index', packageIndexes)
        # print('Distances', distances)
        # print('Actually Packages', truck.packages)

        # print('Distance 0', distances[0])
        # min_distance = distances[0]
        # print(min_distance)
        # or i in range(0, len(distances)):
        # print(distances[i])
        # if distances[i] <= min_distance:
        # min_distance = distances[i]
        # print(min_distance)

        # min distance of package from distance list
        min_distance = min(distances, key=float)
        # print('Min_Distance Found',min_distance)

        indexOfPackage = packageIndexes[distances.index(min_distance)]
        # print('Package Index',indexOfPackage )
        packageDelivered = truck.packages[packageIndexes.index(indexOfPackage)]
        # print('Package ID', packageDelivered)

        # Changing the status of a package from 'En Route' To delivered
        # print('Package Delivered:',packageHashTable.search(packageDelivered))
        Package = packageHashTable.search(packageDelivered)
        # print('Package this is',Package)

        # Updating the time of the program
        timeDelivered = miles_to_time(float(min_distance))
        deliveryTime = add_times(truck.time, timeDelivered)
        truck.time = deliveryTime
        # print(deliveryTime)
        Package.status = f'Delivered, {deliveryTime}'
        # print('Package Delivered:', packageHashTable.search(packageDelivered))

        # Find time package delivered
        # print("Time",miles_to_time(float(min_distance)))
        # Add min distance to total truck miles
        truck.miles += float(min_distance)
        # print('Truck Miles', min_distance)

        truck.currentLocation = indexOfPackage
        # print('New Truck Current Location', indexOfPackage)
        packageIndexes.remove(indexOfPackage)
        truck.packages.remove(packageDelivered)
        distances.clear()
        # print("333333")
        # print('Package Index', packageIndexes)
        # print('Distances', distances)
        # print('Actually Packages', truck.packages)

    # print('Total Truck Miles',truck.miles)
    # print("Truck 1 has delivered all their packages")


# def hashTablePrint(packageHashTable):
# print('Packages:')
# Fetch data from Hash Table
# for i in range(1, len(packageHashTable.table) + 1):
# print("Packages: {}".format(packageHashTable.search(i)))  # 1 to 11 is sent to myHash.search()

# checks to see what is the first two numbers after ,
def check_string(string):
    status = string.split(',')

    if len(status) >= 2:
        characters = status[1].strip()[:5]
        return characters
    else:
        return "Error not delivered yet"


def getTimeForPackages(userInput):
    print(
        f'All package statuses as of {userInput}\n')
    for i in range(1, len(packageHashTable.table) + 1):
        package = (packageHashTable.search(i))  # 1 to 11 is sent to myHash.search()
        if check_string(package.status) < userInput:
            print(
                f'Package ID: {package.packageID}, Delivery Address: {package.address}, Delivery Deadline: {package.deadline},'
                f'Status: {package.status}')
        elif check_string(package.status) > userInput:
            print(
                f'Package ID: {package.packageID}, Delivery Address: {package.address}, Delivery Deadline: {package.deadline},'
                f'Status: En Route')
        elif check_string(package.status) == userInput:
            print(
                f'Package ID: {package.packageID}, Delivery Address: {package.address}, Delivery Deadline: {package.deadline},'
                f'Status: {package.status}')
        elif userInput == 'exit':
            print("Exiting...")


def getTimeForSinglePackages(packageID, userInput):
    print(
        f'Package statuses as of {userInput}\n')
    package = (packageHashTable.search(int(packageID)))  # 1 to 11 is sent to myHash.search()
    if check_string(package.status) < userInput:
        print(
            f'Package ID: {package.packageID}, Delivery Address: {package.address}, Delivery Deadline: {package.deadline},'
            f'Status: {package.status}')
    elif check_string(package.status) > userInput:
        print(
            f'Package ID: {package.packageID}, Delivery Address: {package.address}, Delivery Deadline: {package.deadline},'
            f'Status: En Route')
    elif check_string(package.status) == userInput:
        print(
            f'Package ID: {package.packageID}, Delivery Address: {package.address}, Delivery Deadline: {package.deadline},'
            f'Status: {package.status}')
    elif userInput == 'exit':
        print("Exiting...")


class Main:
    # User Interface
    while True:
        print("\nWelcome to the WGUPS package delivery program")
        userInput = input("Type in start to begin the delivery process and you can press exit to stop the program at "
                          "anytime.\n")
        if userInput == 'start':
            deliverPackages(truck1)
            deliverPackages(truck2)
            # discovered at 10:20 am that package #9 has the wrong address - needs changed to 410 S. State St., Salt Lake City, UT 84111
            userInput = input("Discovered that package 9 has the incorrect address, do you want to fix? Enter y to "
                              "fix and n to"
                              " not fix.\n")
            if userInput == 'y':
                package9 = packageHashTable.search(9)
                package9.address = '410 S. State St.'
                package9.zip = '48111'
                deliverPackages(truck3)
                totalMiles = truck1.miles + truck2.miles + truck3.miles
            elif userInput == 'n':
                deliverPackages(truck3)
                totalMiles = truck1.miles + truck2.miles + truck3.miles

            while True:
                print("***************************************")
                print(
                    '1. Print all of the Packages with Package Status, Package Address, Package Deadline, and Package '
                    'Delivery Time at a certain time')
                print(
                    "2. Get a Single Package with Package Status, Package Address, Package Deadline, and Package "
                    "Delivery"
                    " Time at a certain time")
                print("3. Print the total mileage of all the trucks and see individual miles for each truck")
                print("4. Exit the Program")
                print("***************************************\n")

                # Get Input from user
                userInput = input(
                    "Select an option.\n")
                if userInput == '1':
                    userInput = input(
                        "Please enter a time to show all packages before, at, and after that time. (Please "
                        "input in military time hh:mm)\n")
                    getTimeForPackages(userInput)
                elif userInput == '2':
                    packageID = input("Type in the package you want to search for.\n")
                    userInput = input("Type in the time you want to search for. (Please "
                                      "input in military time hh:mm)\n")
                    getTimeForSinglePackages(packageID, userInput)
                elif userInput == '3':
                    totalMiles = truck1.miles + truck2.miles + truck3.miles
                    print(f"Total Miles Driven: {"%.1f" % totalMiles} miles")
                    print(f"Truck 1 Miles Driven: {"%.1f" % truck1.miles} miles ")
                    print(f"Truck 2 Miles Driven: {"%.1f" % truck2.miles} miles ")
                    print(f"Truck 3 Miles Driven: {"%.1f" % truck3.miles} miles ")
                    print(' \n')
                elif userInput == '4':
                    print("Exiting...")
                    break
                else:
                    print('Unknown Error')
                    break
        else:
            print('Unknown Error')
            break
