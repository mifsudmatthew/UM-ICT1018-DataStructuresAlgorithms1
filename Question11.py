def factorial(n): # Defining a new function which calculates the factorial of a given number 'n'.
    result = 1 # Creating a variable to store the factorial result.
    for x in range(1,n+1): # Looping from 1 to n
        result = result * x # Multiplying 'result' with 'x'.
    return result 

def TrigFunction(funct,angle,terms): # Defining a new function which calculates the sine or cosine of a given angle and a number of terms.
    
    total = 0 # Creating a variable to store the total of the number of terms chosen.

    for x in range(terms): # Looping for the amount of terms chosen.

        SinExpansion = (angle ** (2 * x) / factorial(2*x)) * (-1) ** x # Sine Expansion Formula
        CosExpansion = (angle ** ((2 * x)+1) / factorial((2 * x)+1)) * (-1) ** x # Cosine Expansion Formula

        if(funct == "cos"): # If cosine is chosen.
            total = total + SinExpansion # Each sine term is added to the variable 'total'.
        elif(funct == "sin"): # If sine is chosen.
            total = total + CosExpansion # Each cosine term is added to the variable 'total'.
    
    return total

# Testing both the factorial function and the trigonometric function.
print(f'Factorial of 5: {factorial(5)}')
print(f'Factorial of 0: {factorial(0)}')
print(f'Factorial of -50: {factorial(-50)}')
print(f'Cosine Expansion of angle 2.3 for 10 terms: {TrigFunction("cos",0.3,10)}')
print(f'Cosine Expansion of angle 2.3 for -10 terms: {TrigFunction("cos",-0.3,-10)}')
print(f'Sine Expansion of angle 2.3 for 20 terms: {TrigFunction("cos",0.2,20)}')
