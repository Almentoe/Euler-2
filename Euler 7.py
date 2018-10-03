import math
from math import *
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
    
A = primes    
    
print(A[10000])