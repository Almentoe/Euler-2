import math

def IsPrime(n):
    if n <=1:
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i == 0:
                return False
    return True        

def TruncL(number):
    STRING_number = str(number)
    return (STRING_number[1:])

def TruncR(number):
    REVERSE = str(number)[::-1]
    TRUNC_REVERSE = TruncL(REVERSE)
    TRUNC_number = TRUNC_REVERSE[::-1]
    return TRUNC_number

def TruncLmult(number,mult):
    j=0
    ANSWER = number
    while j < mult:
        ANSWER =(TruncL(ANSWER))
        j+= 1
    return ANSWER

def TruncRmult(number,mult):
    
    j=0
    ANSWER = number
    while j < mult:
        ANSWER = (TruncR(ANSWER))
        j+= 1
    return ANSWER   
        
counter = 0
j = 13
PrimeList = []

def IsTruncPrime(number):
    m = len(str(number))
    while m >=1:
        if IsPrime(int(TruncLmult(number,m-1))) and IsPrime(int(TruncRmult(number,m-1))):
            m = m - 1
            
        else: return False
    return True    
               
while counter < 12:
    while j > 0:
        if IsTruncPrime(j):
            PrimeList += [j,]
            counter = counter + 1
            j = j + 1
        elif counter == 11:
            j = -1
            counter = 12
        else:
            j+= 1
print(sum(PrimeList))           

    