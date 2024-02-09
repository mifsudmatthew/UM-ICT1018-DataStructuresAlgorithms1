def ExtremePoints(array): # Defining a new function 'ExtremePoints'.

    pointsList = [] # Creating an array 'pointsList' to store the extreme points found in 'array'.

    arrayLength = len(array) # Obtaining the length of the array inputted.

    for x in range(1,arrayLength-1): # Looping from the second element till the element prior to the last. (Based on conditions given)

        if((array[x-1]<array[x] and array[x]>array[x+1]) or (array[x-1]>array[x] and array[x]<array[x+1])): # If entry being accessed satisfied the conditions
           pointsList.append(array[x]) # The element is added to 'pointsList'

    pointsLength = len(pointsList) # Obtaining the length of 'pointsList', which corresponds to the number of extreme points found.

    if(pointsLength == 0): # If the list remained empty.
        print("SORTED\n")
    else:
        for x in range(pointsLength): # Looping through all elements of 'pointsList'.
            print(pointsList[x], end=" ") # Outputting the current element being accessed.
        print("\n")
# Yes, an array has no extreme points if and only if it is sorted. 
# This is because if an array is not sorted there must be at least one element which is greater or smaller than both adjacent elements.
# On the other hand, if an array is sorted it is impossible for an element to have adjacent elements which are either both larger or smaller than that specific element.

arr1 = [1,2,3,4,5] # Sorted array
# Two randomly filled arrays
arr2 = [9,2,8,100,3,6,7,2]
arr3 = [34,39,12,28,3,24,12,11,33,62]
arr4 = [] # Empty array
arr5 = [3] # Array with single element
ExtremePoints(arr1)
ExtremePoints(arr2)
ExtremePoints(arr3)
ExtremePoints(arr4)
ExtremePoints(arr5)