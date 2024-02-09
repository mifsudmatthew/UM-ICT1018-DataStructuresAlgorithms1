def sqrtApprox(n): # Defining a new function to calculate the square root of a given number 'n'.

    # x = sqrt(n), x^2 = n ,therefore x^2 - n = 0

    if n<2: # If input is less than 2 then the input is returned back (since the root of 0 and 1 is 0 and 1 respectively, and negative numbers do not have a root)
        return n

    x = n/2 # First guess.

    while True:

        funct = x**2 - n # Storing the square root function in 'funct'.
        deriv = 2*x # Storing the derivative of 'funct' in 'deriv'.
        x_recursive = x - funct / deriv # Using the Newton-Raphson method.

        if abs(x-x_recursive) < 0.0001: # If the difference between the previous and current estimation is less than 0.0001, execution is stopped.
            break

        x = x_recursive # Updating the previous estimation with the value of the new estimation.

    return x_recursive # Returning the last estimation.

print(f'Root of -1: {sqrtApprox(-1)}')
print(f'Root of 0: {sqrtApprox(0)}')
print(f'Root of 1: {sqrtApprox(1)}')
print(f'Root of 2: {sqrtApprox(2)}')
print(f'Root of 100: {sqrtApprox(100)}')