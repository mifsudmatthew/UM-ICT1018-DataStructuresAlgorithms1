def LargestFromList(array): # Defining a new function which finds the largest number from a list.
    if(len(array)==0): # If the list is empty
        return 0
    if(len(array)==1): # If the list contains 1 number.
        return array[0] # The number is returned.
    else: # Otherwise
        return max(array[0],LargestFromList(array[1:])) # Return the largest number from the first number and the rest of the list.

print(f'List: {[1,2,100,2,10,22,1000]} Largest: {LargestFromList([1,2,100,2,10,22,1000])}')
print(f'List: {[1,2,-9,2,10,22,-1000]} Largest: {LargestFromList([1,2,-9,2,10,22,-1000])}')
print(f'List: {[-1,-2,-3,-4,-5]} Largest: {LargestFromList([-1,-2,-3,-4,-5])}')
print(f'List: {[]} Largest: {LargestFromList([])}')
print(f'List: {[-2]} Largest: {LargestFromList([-2])}')
