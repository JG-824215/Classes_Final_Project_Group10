from typing import List


class Facility:
    def __init__(self, facility_name):
        self.facility_name = facility_name

    def addFacility(self):
        with open("facilities.txt", "a") as file:
            file.write("\n")
            file.write(self.facility_name)
        file.close()

def displayFacilities():
    with open("facilities.txt", "r") as file:
        for line in file:
            print(line)
    file.close()
    

def writeListOfFacilitiesToFile(facilities_list: List[Facility]):
    for facility in facilities_list:
        facility.addFacility()
    
def display_f_menu():
    print("Facilities Menu:")
    print("1 - Display Facilities list")
    print("2 - Add Facility")
    print("3 - Back to the Main Menu")
    
    category = int(input())
    if category == 1:
        displayFacilities()
    elif category == 2:
        data = input("Enter Facility name: ")
        facility = Facility(data)
        facility.addFacility()
    elif category == 3:
        return

display_f_menu()