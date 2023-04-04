#Returns the factioral of the parameter 'n' by recursively
#multiplying 'n' by the factorial of 'n-1' until 'n-1' equals 1.
#Default return value of 1 for all 'n' values less than or equal to 1
def factorial(n):
    if (n <= 1):
        return 1
    else:
        return n * (factorial(n-1))



def combinations(n, r):
    if(0 <= r and r >= n):
        return 0
    else:
        return factorial(n) / (factorial(r) * factorial(n-r))

def hypercake(n, k):
    value = 0
    while(k >= 0):
        value = value + combinations(n, k)
        k = k - 1
    return value

print(hypercake(8,3))