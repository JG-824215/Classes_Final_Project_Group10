from typing import List

class Laboratory:
    def __init__(self, lab_name, cost):
        self.lab_name = lab_name
        self.cost = cost

    def __str__(self):
        return f"{self.lab_name}, {self.cost}"

    def addLabToFile(self):
        l_info = self.formatLabInfo()
        with open("laboratories.txt", "a") as file:
            file.write("\n")
            file.write(l_info)
            file.close()

    def formatLabInfo(self):
        lab_info = f"{self.lab_name}_{self.cost}"
        return lab_info

    def readLaboratoriesFile(self):
        with open("laboratories.txt", "r") as file:
            for line in file:
                print(line)
            file.close()

def writeListOfLabsToFile(labs_list: List[Laboratory]):
    for lab in labs_list:
        lab.addLabToFile()


def enterLaboratoryInfo():
    lab_name = input("Enter Laboratory facility: ")
    cost = input("Enter Laboratory cost: ")
    return lab_name, cost

def displayLabsList(file):
    labs = []
    with open(file, "r") as f:
        for line in f:
            lab_name, cost = line.strip().split("_")
            labs.append(Laboratory(lab_name.strip(), cost.strip()))
        f.close()
    for l in labs:
        print(l)

def display_l_menu():
    print("Laboratories Menu: ")
    print("1 - Display laboratories list")
    print("2 - Add laboratory")
    print("3 - back to the Main Menu")

    category = int(input())

    if category == 1:
        displayLabsList("laboratories.txt")

    elif category == 2:
        lab_name, cost = enterLaboratoryInfo()
        lab = Laboratory(lab_name, cost)
        lab.addLabToFile()
    elif category == 3:
        return

display_l_menu()