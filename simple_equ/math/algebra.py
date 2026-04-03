def power(base, exponent):
    return base ** exponent

#Takes a number and until it is equal to 0 it multiplies it with its previous in order storing the new result.
def factorial(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1    
    return result

#Implementation based on the Eucledean algorithm.
def gcd(a, b):
    if b == 0: 
        return a
    return gcd(b, a % b)

#Use Newton's method to closely approximate the square root of a number
def sqrt(number):
    if number > 0:
       x = number 
       tolerance = 0.000000000001

       while True: 
           next = (x + number / x) / 2

           if abs(next - x) < tolerance: 
               return next
           
           x = next
    elif number == 0: 
        return 0; 
    else: 
        raise ValueError("Not a real number")

#Forms of basic linear and quadratic equations
def basic_quadratic(a, b, c): 
    d = (b**2) - (4*a*c)
    sqrt_d = sqrt(d)

    root1 = (-b + sqrt_d) / (2*a)
    root2 = (-b - sqrt_d) / (2*a)
    return root1, root2

def basic_linear(a, b):
    x = -b/a
    return x

def is_divisible(a: int | float, b: int | float) -> bool:
    # Checks if a is divisible by b by checking if the remainder of a divided by b is 0.
    # Raise ValueError if b is zero.

    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b == 0