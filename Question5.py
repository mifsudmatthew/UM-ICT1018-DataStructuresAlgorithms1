class Stack:

    def __init__(self): # Initialising a 'Stack' object, using self to give it properties.
        self.items = [] # Creating a new array which will store the contents of the stack.

    def push(self,input): # Defining a function to push items to the stack.
        self.items.append(input) # Adding a new item to the end of the array.

    def pop(self): # Defining a function to pop items from the stack.
        self.items.pop() # Removing the last item added to the array.
    
    def peek(self): # Defining a function to obtain item at the top of the stack.
        return self.items[-1] # Returning the last item in the array.
    
def ReversePolish(input): # Defining a function which computes reverse polish notation expressions.

    stack = Stack() # Initialising the 'stack' variable with a Stack object.

    chars = input.split() # Splitting up user input into individual characters in an array.

    counter = 0 # Creating a counter to keep track of how many individual items have been accessed from the expression.

    # If the expression has, at least 1 item which is numeric or the first two items are numbers.
    if((len(chars)==1 and chars[0].isnumeric()) or (chars[0].isnumeric() and chars[1].isnumeric())):

        for char in chars: # Iterating through each character in the expression.
            counter = counter + 1 # Incrementing 'counter' by 1

            if(char.isnumeric()): # If the item being accessed is a number.
                stack.push(int(char)) # The number is pushed to the stack.
                
            else: # If the item being accessed is not a number.

                if(len(stack.items)==1): # If there is no second number to be computed with the first number.
                    print("Only 1 number in stack.")
                    break # Stop execution.

                num1 = stack.peek() # Storing the current number at the top of the stack in variable 'num1'.
                stack.pop() # Removing the number at the top of the stack.
                num2 = stack.peek() # Storing the current number at the top of the stack in variable 'num2'.
                stack.pop() # Removing the number at the top of the stack.

                if(char == '+'): # If the item being accessed is a '+'.
                    newNum = num1 + num2 # Add 'num1' and 'num2'.
                elif(char == '-'): # If the item being accessed is a '-'.
                    newNum = num1 - num2 # Subtract 'num2' from 'num1'.
                elif(char == 'x'): # If the item being accessed is a 'x'.
                    newNum = num1 * num2 # Multiplying 'num1' and 'num2'.
                elif(char == '/'): # If the item being accessed is a '/'.
                    if num2 == 0:
                        raise ZeroDivisionError("RPN Expression contains division by 0.")
                    newNum = num1 / num2 # Dividing 'num1' by 'num2'.
                else: # If any other type of character is encountered.
                    raise Exception("Invalid Operator Found")
                
                stack.push(newNum) # The result of the operation is pushed to the stack.
            
            # The following displays the contents of the stack:
        
            trimmedChars = chars[counter:] # Removing the first element (in each iteration) of the RPN expression and storing the result in 'trimmedChars'

            print(f'Stack: ({counter})')
            for x in range(len(trimmedChars)): # Looping through all elements of 'trimmedChars'
                print(trimmedChars[len(trimmedChars)-x-1]) # Printing the elements of 'trimmedChars' in reverse (to resemble a stack).

            for x in range(len(stack.items)): # Looping through all elements of 'trimmedChars'
                print(f'{stack.items[len(stack.items)-x-1]} (Selected)') # Printing the elements currently pushed to the stack in reverse (to resemble a stack).
            print("\n")
            
    else: # Otherwise
        raise Exception("Incorrect RPN Expression.")
ReversePolish("3 6 4 x 5 + -")