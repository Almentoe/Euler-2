
def Collatz(k):
    if k%2 == 0:
        return k//2
    else:
        return 3*k+1
def CollatzList(P):
    n = P
    ColList = ()
    while Collatz(n) > 1:
        ColList = ColList + (Collatz(n),)
        n = Collatz(n)
    if P == 1:
        return (1,)
    else: return(P,) + ColList + (1,)
    
#print(CollatzList(7))
LengthList = ()
n = 1
while n < 1000000:
    LengthList += ((len(CollatzList(n)),n),)
    n = n + 1
print(LengthList)  