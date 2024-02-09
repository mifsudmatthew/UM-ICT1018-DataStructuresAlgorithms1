
def checkPrime(num): # Defining a function to test if a number is prime.

    if (num < 2): # If a number is less than 2, then it cannot be a prime number.
        return False
    else: # Otherwise
        for x in range(2,int(num**0.5)+1): # Looping from 2 to the square root of 'num' ('num' to the power of 1/2). 
            if(num%x==0): # If 'x' can divide exactly 'num', then 'num' is not a prime number.
                return False
    
    return True # Otherwise the 'num' must be a prime number. 

# Optimisations: The for loop was made to loop until the square root of the inputted number. This is because if a number is
#                not prime at least one if its factors must be smaller than or equal to its square root. Therefore if a factor less
#                than or equal to the square root is not found, the inputted number must be prime.

def SieveOfEratosthenes(num): # Defining a function to perform the Sieve of Eratosthenes for all numbers up to 'num'.

    if(num>1): # If 'num' is strictly greater than 1

        booleanArray = [] # Creating an array to store booleans which keep track of prime numbers.
        for x in range(0,num+1): # Looping through all numbers up to 'num'.
            booleanArray.append(True) # Appending boolean True to 'booleanArray'

        booleanArray[0] = booleanArray[1] = False # Setting, 0 and 1 as boolean False, since they are not prime numbers.

        for x in range(2,int(num**0.5)+1): # Looping from 2 till the square root of 'num' (same optimisation as mentioned prior).
            if(booleanArray[x]): # If the element being accessed is a boolean True.
                for y in range(x**2,num+1,x): # Looping: y = x^2, x^2 + x, x^2 + 2x, x^2 + 3x, ..., not exceeding 'num'.
                    booleanArray[y] = False # Setting non-prime numbers to boolean False.

        primeArray = [] # Creating an array to store prime numbers.
        primeLength = len(booleanArray) # Obtaining the length of 'primeArray'.
        for x in range(primeLength): # Looping through each prime number index.
            if(booleanArray[x]): # If the boolean value of current index being accessed is True.
                primeArray.append(x) # Append the index to 'primeArray'

        return primeArray

# Optimisations: 1. Multiples of each prime number x were marked from x^2. This is because smaller multiples are already marked by a smaller prime number.
#                2. A list of booleans instead of numbers was used to save memory.
#                3. Looping until the square root of 'num' (which is faster).

print(f'27 Prime? {checkPrime(27)}')
print(f'29 Prime? {checkPrime(29)}')
print(f'Sieve of Eratosthenes until 0: {SieveOfEratosthenes(0)}')
print(f'Sieve of Eratosthenes until -1: {SieveOfEratosthenes(-1)}')
print(f'Sieve of Eratosthenes until 2: {SieveOfEratosthenes(2)}')
print(f'Sieve of Eratosthenes until 27: {SieveOfEratosthenes(27)}')