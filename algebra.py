def power(base, exponent):
    return base ** exponent

def factorial(number):
    #Takes a number and until it is equal to 0 it multiplies it with its previous in order storing the new result
    result = 1
    while number > 0:
        result *= number
        number -= 1    
    return result

print(factorial(5))