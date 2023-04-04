import time


factorialDict = {}
#Returns the factioral of the parameter 'n' by recursively
#multiplying 'n' by the factorial of 'n-1' until 'n-1' equals 1.
#Default return value of 1 for all 'n' values less than or equal to 1
def factorial(n):
    if (n <= 1):
        return 1
    elif(factorialDict.get(n) is not None):
        return factorialDict.get(n)
    else:
        newFactorial = n * (factorial(n-1))
        time.sleep(1)
        print("Adding factorial to dictionary:", str(n) + "! =", newFactorial)
        factorialDict[n] = newFactorial
        return newFactorial
    # end if
# end def



def combinations(n, r):
    if(0 <= r and r >= n):
        return 0
    else:
        return factorial(n) / (factorial(r) * factorial(n-r))
    #end if
# end def

def hypercake(n, k):
    value = 0
    while(k >= 0):
        value = value + combinations(n, k)
        k = k - 1
    # end while
    return value
#end def

def main():
    print("Welcome to the Hypercake Problem Calculator via Python3\n")

    print("The Hypercake Problem can be defined as such:")
    print("\"What is the maximum number of peices which a hypercake")
    print("(a disc generalized to having two or more dimensions defined as \'k\') can be cut")
    print("into using n-many hyperplanar (k minus 1-dimensional) cuts?\n")

    print("Follow the steps below to calculate the maximum cuts for a given hypercake.\n\n")

    while(1):
        nValue = input("1. Enter the number of cuts to use as an integer value (n): ")

        try:
            nValue = int(nValue)
        except:
            print("Invalid n value input. Please try again.")
            continue
        # end try

        kValue = input("2. Enter the number of dimensions the hypercake has as an integer value (k): ")

        try:
            kValue = int(kValue)
        except:
            print("Invalid k value input. Please try again.")
            continue
        # end try


        print("Calculating...Please wait")
        time.sleep(.3)
        print("Hypercake value:",hypercake(nValue,kValue))

        repeat = input("Would you like to try again? (y/N): ")

        while(1):
            if(repeat.lower() == "n" or repeat.lower() == "y"):
                break              
            else:
               repeat = input("Invalid response. Enter \'y\' or \'n\': ")
               continue
            # end if
        # end while

        if(repeat.lower() == "n"):
            break
        # end if
    # end while
# end def

if __name__ == "__main__":
    main()
