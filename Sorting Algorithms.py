# Aliza Grabowski
# Sorting Algorithms
# This file imports the different sorting algorithms to utilize

from MergeSort import *
from QuickSort import *

array = [5,3,2,1,4]
currentSorts= ["Merge Sort", "Quick Sort"]

def checkChoice(sort):
    for i in currentSorts:
        if i == sort:
            return True
    return False

def chooseASort():
    choice = False # used to check if the input is a valid algorithm 
    # loop to make sure user inputs a valid input
    while choice is False:
        print("  Choose a Sorting Algorithm:")
        for x in currentSorts:
            print("\t- ",x)
        sort = input()
        sort = sort.title()
        choice = checkChoice(sort)
        if choice is True:
            print("Thank you.")
            print("---------")
            print("You want to sort with ", sort, " (Y/N)" )
            check = input()
            if check == "Y" or "y":
                return
            else:
                choice = False
        else:
            print("Sorry, invalid input.")
            print("Please try again.")
            print("-----------")

    return

print("Sorting Algorithm Demo".center(40,'-'))
chooseASort()
print("Input a string of numbers you'd like to sort.")
array = input()


