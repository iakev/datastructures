def power_of_2(n):
    if n == 0:
        return  1
        
    return 2* power_of_2(n -1)

print(power_of_2(5))

def sum_integers(n):
    if n == 1:
        return 1
    return n + sum_integers(n-1)

print(sum_integers(3))

def factorial(n):
    """
    Calculate n!
    
    Args:
       n(int): factorial to be computed
    Returns:
       n!
    """
    
    # TODO: Write your recursive factorial function here
    
    if n == 0:
        return 1

    return n * factorial(n-1)


print(factorial(5))