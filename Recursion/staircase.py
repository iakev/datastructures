"""
param: n - number of steps in the staircase
Return number of possible ways in which you can climb the staircase
"""
# def staircase(n):
#     '''Hint'''
#     # Base Case - What holds true for minimum steps possible i.e., n == 0, 1, 2 or 3? Return the number of ways the child can climb n steps.
#     if n <= 3:
#         if n == 0:
#             return 0

#         if n == 1:
#             return 1

#         if n == 2:
#             return 2
#         if n == 3:
#             return 4

#     # Recursive Step - Split the solution into base case if n > 3.
#     else:
#         steps = staircase(n-1)
#         steps += 1

#     return steps

##############udacity solution
def staircase(n):
    if n <= 0:
        return 1
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)
    
print(staircase(5))