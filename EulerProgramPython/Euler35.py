#The number, 197, is called a circular prime because all rotations
# of the digits: 197, 971, and 719, are themselves prime.
#
#There are thirteen such primes below 100: 2, 3, 5, 7, 11,
# 13, 17, 31, 37, 71, 73, 79, and 97.
#
#How many circular primes are there below one million?

import math
import itertools

def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if n%i == 0:
      return False
  return True
N = 1000000
primes = ()
for num in range(2,N):
  if is_prime(num):
    primes = primes + (num,)

PRIMES = primes   
PRIMES = set(PRIMES)

def number_to_list(Number):
    LIST = []
    index = 0
    Number = str(Number)
    while index < len(Number):
        LIST += [int(Number[index])]
        index += 1
    return LIST

def list_to_number(List):
    
#    Takes in a list of numbers and outputs a number:
    number = ""
    counter = 0
    while counter < len(List):
        number += str(List[counter])
        counter += 1
    return int(number)

def push_1(Number):
    Number_list = number_to_list(Number)
    index = 0
    Cycled_list = []
    if len(Number_list) > 1:
        
        
        while index < len(Number_list)-1:
            Cycled_list += [Number_list[index+1],]
            index += 1
        return list_to_number(Cycled_list + [Number_list[0],])
    else:
        return Number
    return list_to_number(Cycled_list + [Number_list[0],])

def push_n(Number,n):
    Output = Number
    iterate = 0
    while iterate < n:
        Output = push_1(Output)
        iterate += 1
    return Output

def is_cycle_prime(prime):
    index = 0
    while index < len(str(prime)):
        
        Bool = True
        if not "0" in str(prime) and push_n(prime,index) in PRIMES:
            index += 1
        else:
            Bool = False
            break
    return Bool
Cycle_Primes_List = []
for x in PRIMES:
    if is_cycle_prime(x):
        Cycle_Primes_List += [x,]
        
print(len(Cycle_Primes_List))



            
        
        