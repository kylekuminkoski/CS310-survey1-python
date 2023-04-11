# CS310-survey1-python

This is a Python script I wrote for a class assignment. The script takes n-many slices and k-many dimensions from the user and calculates the maximum number of peices the hypercake can be sliced into. The functionality is achieved using factorials and combinations within recursive methods.

The factorial method is "memoized" which means it has been optimized for speed in exchange for memory usage. This can be seen in the code's usage of a dictionary that updates its entries as new factorials are calculated within the script.

The script will run continuously, allowing for multiple usages within a single session, until the user opts to exit.


# Example Output
Welcome to the Hypercake Problem Calculator via Python3  
  
The Hypercake Problem can be defined as such:  
"What is the maximum number of peices which a hypercake  
(a disc generalized to having two or more dimensions defined as 'k') can be cut  
into using n-many hyperplanar (k minus 1-dimensional) cuts?  
  
Follow the steps below to calculate the maximum cuts for a given hypercake.  
  
  
1. Enter the number of cuts to use as an integer value (n): 9  
2. Enter the number of dimensions the hypercake has as an integer value (k): 5  
Calculating...Please wait  
Adding factorial to dictionary: 2! = 2  
Adding factorial to dictionary: 3! = 6  
Adding factorial to dictionary: 4! = 24  
Adding factorial to dictionary: 5! = 120  
Adding factorial to dictionary: 6! = 720  
Adding factorial to dictionary: 7! = 5040  
Adding factorial to dictionary: 8! = 40320  
Adding factorial to dictionary: 9! = 362880  
  
Hypercake value: 382.0  
  
Would you like to try again? (y/N): y  
1. Enter the number of cuts to use as an integer value (n): 9  
2. Enter the number of dimensions the hypercake has as an integer value (k): 3  
Calculating...Please wait  
  
Hypercake value: 130.0  
  
Would you like to try again? (y/N): exi  
Invalid response. Enter 'y' or 'n': y  
1. Enter the number of cuts to use as an integer value (n): 8  
2. Enter the number of dimensions the hypercake has as an integer value (k): 3  
Calculating...Please wait  
  
Hypercake value: 93.0  
  
Would you like to try again? (y/N): n  
goodbye.
