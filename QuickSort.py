# Aliza Grabowski
# Quick Sort Algorithm
# Steps:
#       1.Take in an array of numbers
#       2.Choose a pivot point (typically last element)
#       3.Set less than pointer(x)and greater than pointer(swap)
#       4.Based on pivot filter others as if less than (increment less than pointer) and greater than (Swap)
#       5.Recursive

# array = [5,3,2,1,4]
# low = 0
# high = None
# define the partition position function
def partition(array, low, high):
    # Grab the rightmost element and set as the pivot point 
    pivotPoint = array[high]
    # print("pv = ", pivotPoint)
    swapPointer =  low - 1
    

    # After grabbing the Pivot Point, Sort through the list and check each element
    # if element is greater than Pivot Point Swap & move smaller pointer to next element
    # if element is Less than move to next element
    for x in range(low,high):
        if array[x] <= pivotPoint:
            swapPointer = swapPointer + 1
            
            # swap elements
            (array[swapPointer],array[x])= (array[x],array[swapPointer])

    # swap pivot point with the larger element found by the swapPointer
    (array[swapPointer + 1], array[high]) =  (array[high],array[swapPointer + 1])       

    return swapPointer + 1

# Define quick sort function 
# Must take in an array, a low number, and high number to allow recursive to work
def quickSort(array, low, high):
    # print("array =",array)
    # check to see if high = None - if so set as last element in array
    if high is None:
        high = len(array)-1

    # check to see if low = None - if so set to 0
    if low is None:
        low = 0
    # make sure low is smaller than high
    if low < high:
        # Find the pivot index
        # smaller to left & larger to right
        pivotIndex = partition(array,low,high)

        # recursive smaller / left of pivot index 
        quickSort(array, low, pivotIndex - 1)

        # recursive larger / right of pivot index
        quickSort(array, pivotIndex + 1, high)
    
    return

# quickSort(array,low,high)