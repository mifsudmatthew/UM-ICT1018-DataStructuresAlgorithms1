from random import randint
from random import sample

# Array size range chosen: 256 - 512 elements.
randomRanges = sample(range(256,513),2) # Generating two random unique numbers between 256 and 512 in an array.
arrayA_size = randomRanges[0] # Storing the first random number in 'arrayA_size'.
arrayB_size = randomRanges[1] # Storing the second random number in'arrayB_size'.

arrayA = [] # Creating the first array
arrayB = [] # Creating the second array

# Populating 'arrayA' with integers between 0 and 1024.
for x in range(arrayA_size): # Looping from 0 until the value of 'arrayA_size' - 1;
    arrayA.append(randint(0,1024)) # Appending a random number between 0 and 1024 to 'arrayA'.

# Populating 'arrayB' with integers between 0 and 1024.
for x in range(arrayB_size): # Looping from 0 until the value of 'arrayB_size' - 1.
    arrayB.append(randint(0,1024)) # Appending a random number between 0 and 1024 to 'arrayB'.

print("Array A (unsorted):\n")
print(arrayA)

print("\nArray B (unsorted):\n")
print(arrayB)

def ShellSort(array): # Defining a new function 'ShellSort'.

    arrayLength = len(array) # Obtaining the length of the array inputted as a parameter.

    distance = arrayLength // 2 # Finding the length of half the array (distance).

    while distance >= 1: # Looping while the distance between two elements compared is at least 1.

        for x in range(distance, arrayLength): # Looping from the element 'distance' of the array till the last element of the array.

            tmp = array[x] # Storing the current element being accessed in variable 'tmp'.
            y=x
            while y >= distance and array[y-distance] > tmp: # Looping while the index of the element being accessed is greater or equal to the 'distance' & the element which is 'distance' elements apart is greater than the value of the current element being accessed.

                array[y] = array[y-distance] # The current element takes the value of the element 'distance' elements away.
                y = y - distance # Updating the value of 'y' to the element 'distance' elements away.
            array[y] = tmp # This element then, takes the value of the original element.
    
        distance = distance // 2 # Halving the gap between the two elements which will be swapped next.

    return array

def QuickSort(array): # Defining a new function 'QuickSort'.

    arrayLength = len(array) # Obtaining the length of the array inputted as a parameter.

    if arrayLength < 2: # If the array has a length of 0 or 1

        return array # The array is returned as is.
    
    else:

        pivotElement = array[0] # A pivot element is chosen (the first element). All elements will be compared to this element for sorting.
        leftList = [] # An array created to store elements that are smaller than the element chosen as a pivot.
        rightList = [] # An array creted to store elements that are larger than the element chosen as a pivot.

        for x in range(1,arrayLength): # Loop through all elements except the pivot element.

            if(array[x]<pivotElement): # If the current element is smaller than the pivot element.
                leftList.append(array[x]) # The element is appended to the 'leftList' array.
            else: # If the current element is larger than the pivot element.
                rightList.append(array[x]) # The element is appended to the 'rightList' array.
            
        # The lists are combined since all elements in 'leftList' are smaller than the pivot and all element in 'rightList' are larger than the pivot. 
        return QuickSort(leftList) + [pivotElement] + QuickSort(rightList) # The 'QuickSort' algorithm is then applied to both 'leftList' and 'rightList'. 

sortedA = ShellSort(arrayA) # Storing the sorted version of 'arrayA' in 'sortedA'.
sortedB = QuickSort(arrayB) # Storing the sorted version of 'arrayB' in 'sortedB'.


print("\nArray A (Shell Sort):\n")
print(sortedA)

print("\nArray B (Quick Sort):\n")
print(sortedB)