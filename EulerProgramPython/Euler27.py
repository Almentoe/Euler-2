import math
def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if n%i == 0:
      return False
  return True
ENDLOW = 1001
ENDHIGH = 2200000
PRIMESHIGH = [x for x in range(1,ENDHIGH) if is_prime(x)]
PRIMESLOW = [x for x in range(1,ENDLOW) if is_prime(x)]
PRIMESSETHIGH = {x: x for x in PRIMESHIGH}
PRIMESSETLOW = {x: x for x in PRIMESLOW}


def polynomial(a,b,x):
    return x**2 + a*x + b

def is_prime_check(n):
    return n in PRIMESSETHIGH

def polynomial_primes_list_length(a,b):
    x = 0
    primes_list = []
    while x <= 1000:
        if polynomial(a,b,x) in PRIMESSETHIGH:
            primes_list = primes_list + [x,]
            x = x + 1
        else:
            x = 1001
    return len(primes_list)
  
def polynomial_b_list_max_length(b):
    length_primes_list = []
    a = -1000
    while abs(a) <= 1000:
        length_primes_list = length_primes_list + [(polynomial_primes_list_length(a,b),a),]
        a = a+1
    return length_primes_list



#print(polynomial_b_list_max_length(971))
#while 
print(-61*971)

# a = -61 for length 71
#max_length_list_for_b = []

#for b in PRIMESLOW:
#    m = polynomial_b_list_max_length(b)
#    if m > 70:
#        max_length_list_for_b = max_length_list_for_b + [(m,b),]
        
    
#print(max_length_list_for_b) 
#max b = 971, for a prime length list of 71
#print(polynomial_primes_list_length(1,41))          
            
#print(is_prime_check(400))
#print(PRIMESSET)