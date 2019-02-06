def Triangular(n):
    return int((n*(n+1))/2)

def NumberFactors(n):
    j = 1
    Factors = ()
    while j <= n:
        if (n//j)*j == n:
            Factors = Factors + (j,)
            j = j + 1
        else:
            j = j + 1
    return len(Factors) 
n = 1
L = NumberFactors(2)
M = NumberFactors(1)
while int((L*M)) <600:
    
    if (n//2)*2 == n:
        L = NumberFactors(n//2)
        M = NumberFactors(n+1)
        #print(L*M,Triangular(n))
        if L*M > 500:
            print(L*M,Triangular(n))
        n = n+1
    else:
        L = NumberFactors(n)
        M = NumberFactors((n+1)//2)
        if L*M > 500:
            print(L*M,Triangular(n))
        #print(L*M,Triangular(n))
        n = n+1
        
#print(Triangular(21737))       
#print (NumberFactors(4))       