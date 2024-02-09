import csv

def CollatzSequence(num): # Defining a new function to compute the Collatz Sequence for a specific number.

    collatzSeq = [num] # Creating a new array containing the variable 'num'.

    while (num!=1): # Looping while 'num' is not equal to 1.

        if(num%2==0): # If 'num' is even.
            num = int(num/2) # Divide num by 2.
        else: # If 'num' is odd.
            num = int((3*num)+1) # Multiply 'num' by 3 and add the result by 1.

        collatzSeq.append(num) # Adding the new value of 'num' to 'collatzSeq' array.

    return collatzSeq

with open('Collatz_Sequences.csv',mode='w',newline='') as file: # Creating a new '.csv' file
    newFile = csv.writer(file) # Creating a variable 'newFile', used to write the sequences to the '.csv' file.

    for x in range(2,513): # Looping from 2 to 512.
        seq = CollatzSequence(x) # Calculating the Collatz sequence of the current value of 'x'.
        newFile.writerow(seq) # Writing the sequence 'seq' to the '.csv' file.
