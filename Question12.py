def FibonacciSum(n): # Defining a new function to calculate the sum of the fibonacci sequence up to 'n' numbers.

    if (n <= 0): # If 'n' is equal to 0.
        return 0
    elif (n == 1): # If 'n' is equal to 1.
        return 1
    else: # Otherwise.
        #If n = 2.
        num1 = num2 = 1 # The first two digits are initialised.
        sum = num1 + num2 # Their sum is calculated.

        #If n > 2.
        for x in range(3,n+1): # Looping from 3 to 'n'.
            num3 = num1 + num2 # Calculating the next term in the fibonacci sequence.
            sum = sum + num3 # Calculating the sum of the previous terms, with the newly calculated term.
            num1 = num2 # Setting 'num1' to 'num2'
            num2 = num3 # Setting 'num2' to the newly calculated term 'num3'.

    return sum

print(f'Fibonacci Sum of 20 :{FibonacciSum(20)}')
print(f'Fibonacci Sum of -7 :{FibonacciSum(-7)}')
print(f'Fibonacci Sum of 0 :{FibonacciSum(0)}')
print(f'Fibonacci Sum of 100 :{FibonacciSum(100)}')
