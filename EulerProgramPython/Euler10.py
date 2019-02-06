import math
from math import *
def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if n%i == 0:
      return False
  return True
N = 2000000
sumprimes = 0
for num in range(2,N):
  if is_prime(num):
    sumprimes = sumprimes + num
    
A = sumprimes
print(A)