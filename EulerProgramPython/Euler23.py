#import math
#def SumOfTuple(G):
#    SumTuple = 0
#    k = 0
#    while k < len(G):
#        SumTuple = SumTuple + G[k]
#        k = k +1
#    return SumTuple    
#    
#def DivisorTuple(n):
#    # Takes in a number, and spits out the proper divisors of the number
#    Divisors = ()
#    k = 2
#    while k < int(math.sqrt(n)) +1:
#        if n%k == 0 and k**2 != n:
#            Divisors = Divisors + (k,n//k)
#            k = k+1
#        elif  n%k == 0 and k**2 == n:
#            Divisors = Divisors + (n//k,)
#            k = k + 1
#        else: k = k+1
#    return Divisors +(1,)  
#
#def SumOfDivisors(n):
#    return SumOfTuple(DivisorTuple(n))
#
#m = 1
#AbunderooNumbers = ()
#while m<30000:
#    if m < SumOfDivisors(m):
#        AbunderooNumbers = AbunderooNumbers + (m,)
#        m = m + 1
#    else:
#        m = m + 1
#x = 0
#while x < len(AbunderooNumbers):
#    
#    y=0
#    while y < len(AbunderooNumbers):
#        print(AbunderooNumbers[x]+AbunderooNumbers[y],x,y)
#        y = y+1
#    x = x + 1
#
##print(SumAbunderooNumbers)        
#print(AbunderooNumbers)       

def GetSumOfDivs(n):
    i = 2
    upper = n
    total = 1
    while i < upper:
        if n%i == 0:
            upper = n/i
            total += upper
            if upper != i: total += i
        i += 1
    return total


def isabundant(n): return GetSumOfDivs(n) > n
lAbundants = [x for x in range(12, 28123) if isabundant(x) == True]
dAbundants = {x:x for x in lAbundants}

sums = 1
for i in range(2, 28123):
    
    boo = True
    
    for k in lAbundants:
        
        if k < i:
            
            if (i-k) in dAbundants:
                boo = False
                break
        else : break
    if boo == True: sums += i

print(sums)