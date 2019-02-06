import math
#def DivisorTupleForRecurringDigits(n,a):
#    # Takes in a number, and spits out the proper divisors of the number
#    Divisors = []
#    k = 2
#    Generator = 1000
#    L = Generator
#    while k < int(math.sqrt(n)) +1:
#        if len(str(n//k)) == a and k<L and n%k == 0 and k**2 != n :
#            Divisors = Divisors + [(k,n//k),]
#            k = k+1
#        elif len(str(n//k)) == a and k < L and n%k == 0 and k**2 == n and len(str(k**2)) == a:
#            Divisors = Divisors + [(n//k,),]
#            k = k + 1
#        else: k = k+1
#    return  Divisors 

#from math import *
#def is_prime(n):
#  for i in range(2,int(math.sqrt(n))+1):
#    if n%i == 0:
#      return False
#  return True
#N = 1000
#primes = ()

def divideNines(n):
    # this function divides the smallest number of the form 999...9 which has n as a factor by n
    assert n % 2 > 0
    assert n % 5 > 0
    # if n is divisible by 2 or 5 it will break the function.
    remainder = 9%n
    quotient = 9//n
    number = ""
    while remainder > 0:
#        print(quotient)
        quotient = (10*remainder + 9)//n
        remainder  = (10*remainder + 9)%n
        number = number + str(quotient)
    return (str(9//n) + number)   
n = 2
while n < 1000:
    if n%2 > 0 and n%5 > 0 and len(divideNines(n))> 900:
        print(len(divideNines(n)),n)
        n = n + 1
    else:
        n = n + 1
        
        

#l = 19
#print(divideNines(l))
#print(1/l)
#print(DivisorTupleForRecurringDigits(10**a - 1,a))

    