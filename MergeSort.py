# Aliza Grabowski
# Merge Sort
# Steps:
#       1. Divide array in half(ish) into 2 sub arrays
#       2. Merge sort will recursively call itself for both halves
#       3. Divide first half of sub array into more sub arrays until sub array contain one element
#       4. Merge together placing the smaller value first

# array = [5,3,2,1,4]
def mergeSort(array):
    # print("array =",array)

    # Check to see if the array is only one element long
    if len(array) <= 1:
        return array
    
    if len(array) > 1:
    
        # First find the middle of the array
        middle = len(array)//2

        # Break the array into two halves
        left = array[:middle]
        right = array[middle:]

        # Recursive the each half starting with the left
        mergeSort(left)
        mergeSort(right)

        # set pointers to 0
        
        i = j = k = 0

        # Create temporary arrays for the left and right side
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i = i + 1
            else:
                array[k] = right[j]
                j = j + 1
            k = k + 1

        # Check if any elements remain
        while i < len(left):
            array[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            array[k] = right[j]
            j = j + 1
            k = k + 1



    
# mergeSort(array)
# print("array =",array)