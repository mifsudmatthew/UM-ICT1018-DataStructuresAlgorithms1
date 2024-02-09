def listDuplicates(array): # Defining a new function which creates a list of numbers that are duplicates in the parameter 'array'.

    encounteredList = {} # Creating a dictionary 'encounteredList' to store how many times a number occurs in 'array'.
    duplicatesList = [] # Creating an array to store 1 copy of each duplicate number found in 'array'.

    for element in array: # Looping through every element in 'array'.

        if (element in encounteredList): # If the element exists in dictionary 'encounteredList'.
            encounteredList[element] = encounteredList[element] + 1 # Incrementing the value of the number of occurrences by 1.
        else:
            encounteredList[element] = 1 # Setting the number of occurrences to 1.

    for num in encounteredList: # Looping through each number in 'encounteredList'.

        if (encounteredList[num] > 1): # If the number of occurrences of 'num' is greater than 1.

            duplicatesList.append(num) # The number is then added to 'duplicatesList'
    
    return duplicatesList

print(f'List: {[1,2,3,4,4,4,5,5,1,1,3,4,5]} Duplicates: {listDuplicates([1,2,3,4,4,4,5,5,1,1,3,4,5])}')
print(f'List: {[]} Duplicates: {listDuplicates([])}')
print(f'List: {[1]} Duplicates: {listDuplicates([1])}')
print(f'List: {[10,100,1000,10000,100000,1000000,1000000]} Duplicates: {listDuplicates([10,100,1000,10000,100000,1000000,1000000])}')
print(f'List: {[-1,1,1,-1,0,2,3,5]} Duplicates: {listDuplicates([-1,1,1,-1,0,2,3,5])}')