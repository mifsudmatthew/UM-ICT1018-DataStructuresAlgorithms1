intList = [] # Creating an array to store integers between 1 and 1024.
Product_Dictionary = {} # Creating a dictionary, to store all possible products for the integers in 'intList'.
Product_Pairs = [] # Creating an array, to store pairs of products which are equal.

loopTimes = None # Creating a variable to store the number of integers that will be inputted.

while loopTimes is None: # Looping while 'loopTimes' remains 'None'
    try:
        loopTimes = int(input("Enter amount of numbers to input:")) # Requesting user input for an integer.
    except ValueError: # If user input is not an integer "Try again." is outputted.
        print("Try again.")

for x in range(loopTimes): # Looping for as many times as chosen in the previous while loop.
    userinput = None # Creating a variable 'userinput' and giving it a null value.
    while userinput is None: # Looping while 'userinput' remains 'None'
        try:
            userinput = int(input(f'Enter integer {x+1}:\n')) # Requesting user input for an integer.
            if(userinput<1 or userinput>1024): # If the inputted number is not in the range of 1 - 1024.
                print("Input out of range (1 - 1024)")
                userinput = None # The 'userinput' is set to None, such that the execution remains in the loop.
            for num in intList: # Looping through the array of inputted integers.
                if(userinput==num): # Checking if the input matches any number previously inputted.
                    print("Number already inputted.")
                    userinput = None # If a number is found, 'userinput' is set to None, such that the execution remains in the loop.
        except ValueError: # If user input is not an integer "Try again." is outputted.
            print("Try again.")
    intList.append(userinput) # Adding each number to 'intList'.

intList_Length = len(intList) # Obtaing the length of 'intList'

for x in range(intList_Length): # Looping through each element of 'intList'

    for y in range(x+1,intList_Length): # Looping through every integer in 'intList' that comes after the element being accessed by the first for loop.
         
        prod = intList[x] * intList[y] # Calculating the product of two distinct integers.

        if prod in Product_Dictionary: # If the product already exists in the dictionary.
            Product_Dictionary[prod].append((intList[x],intList[y])) # The two integers are appended to the other two corresponding integers (which have the same product).
        else: # If the product does not exist
            Product_Dictionary[prod] = [(intList[x],intList[y])] # The two integers are added to the dictionary.

for DictionaryKey in Product_Dictionary: # Looping through each product in 'Product_Dictionary'.
    
    productLength = len(Product_Dictionary[DictionaryKey]) # Obtaining how many pairs the current product has.

    if(productLength>1): # If the product has at least 2 pairs.
         
         numberOfPairs = len(Product_Dictionary[DictionaryKey]) # Obtaining the number of pairs that have the same product.

         for x in range(numberOfPairs): # Looping through each pair of the product being accessed.

            for y in range(x+1,numberOfPairs): # Looping through every product in 'Product_Dictionary' that comes after the product being accessed by the first for loop.

                Product_Pairs.append((Product_Dictionary[DictionaryKey][x],Product_Dictionary[DictionaryKey][y])) # Appending two pairs of integers which are equal when multiplied to 'Product_Pairs'.

totalNumOfPairs = len(Product_Pairs) # Obtaining the total number of pairs.

if(totalNumOfPairs==0): # If no pairs are found.
    print("No Pairs Found")

for x in range(totalNumOfPairs): # Looping through every pair.
    print(Product_Pairs[x]) # Printing the current pair being accessed.