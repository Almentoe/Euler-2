#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
#Find the sum of all numbers which are equal to the sum 
#of the factorial of their digits.
#
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.

# Want a function that computes the factorial of the digits
import math
def factorial_digits_sum(number):
    ARGUMENT = str(number)
    scan = 0
    Fsum = 0
    while scan < len(ARGUMENT):
        Fsum += math.factorial(int(ARGUMENT[scan]))
        scan += 1
    return Fsum

def bool_digit_factorial(number):
    return number == factorial_digits_sum(number)
i = 3
while i < 3*10**7:
    if bool_digit_factorial(i):
        print(i)
        i += 1
    else:
        i += 1
        
print(6*math.factorial(9))