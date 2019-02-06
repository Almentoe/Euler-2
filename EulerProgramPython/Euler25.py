def Fib(n):
    if n <= 1:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)
n = 2
#print(Fib(4))
FibList = () 
A = 0
B = 1
while len(str(B)) <= 1000:
    A , B = B , A+B


    if len(str(B)) == 1000:
#        print(n,B)
        FibList = FibList + (n,)
        n = n+1
    else: 
#        print(n,B)
        n = n+1    
print(FibList)