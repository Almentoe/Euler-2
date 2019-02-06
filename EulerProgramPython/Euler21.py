import math
def SumOfTuple(G):
    SumTuple = 0
    k = 0
    while k < len(G):
        SumTuple = SumTuple + G[k]
        k = k +1
    return SumTuple    
    
def DivisorTuple(n):
    # Takes in a number, and spits out the proper divisors of the number
    Divisors = ()
    k = 2
    while k < int(math.sqrt(n)) +1:
        if n%k == 0 and k**2 != n:
            Divisors = Divisors + (k,n//k)
            k = k+1
        elif  n%k == 0 and k**2 == n:
            Divisors = Divisors + (n//k,)
            k = k + 1
        else: k = k+1
    return Divisors +(1,)  

def SumOfDivisors(n):
    return SumOfTuple(DivisorTuple(n))

def IsAmicable(x,y):
    if SumOfDivisors(x) == y and SumOfDivisors(y) == x:
        return True
    else:
        return False

for x in range(1,10000):
    for y in range(1,x):
        if x!= y and IsAmicable(x,y):
            print(x,SumOfDivisors(x))

#print(DivisorTuple(60))
#print(SumOfDivisors(60))
#print(DivisorTuple(56))
#print(SumOfTuple((1,1,4,1,1,1)))
#print(SumOfDivisors(220))