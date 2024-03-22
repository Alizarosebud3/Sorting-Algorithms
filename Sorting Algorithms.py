# Aliza Grabowski
# Sorting Algorithms
# This file imports the different sorting algorithms to utilize

from MergeSort import *
from QuickSort import *

currentSorts= ["Merge Sort", "Quick Sort"]

def checkChoice(sort):
    for i in currentSorts:
        if i == sort:
            return True
    return False

def chooseASort():
    confirm = False # used to check if the input is a valid algorithm 
    # loop to make sure user inputs a valid input
    while confirm is False:
        print("  Choose a Sorting Algorithm:")
        for x in currentSorts:
            print("\t- ",x)
        sort = input()
        sort = sort.title()
        confirm = checkChoice(sort)
        if confirm is True:
            print("Thank you.")
            print("---------")
            print("You want to sort with", sort, " (Y/N)" )
            check = input()
            if check == "Y" or check == "y":
                return sort
            else:
                confirm = False
        else:
            print("Sorry, invalid input.")
            print("Please try again.")
            print("-----------")
    return

def grabUserArray():
    confirm = False
    while confirm is False:
        print("Input a string of numbers you'd like to sort. Separated by spaces. i.e. '5 3 2 1 4'")
        numbers = input()
        
        # make the user input in array form
        array =  list(map(int, numbers.strip().split()))
        print("Would you like to proceed with array:",array, "(Y/N)")
        check = input()
        if check == "Y" or check == "y":
            return array
        else:
            confirm = False
    
    return

def runSort(sort,array):
    if sort == "Quick Sort":
        quickSort(array,None,None)
        print("Quick Sort Array:",array)
    if sort == "Merge Sort":
        mergeSort(array)
        print("Merge Sort Array:",array)
    return
    
print("Sorting Algorithm Demo".center(90,'-'))
sort = chooseASort()
array = grabUserArray()
runSort(sort,array)
print("Thank You!")




