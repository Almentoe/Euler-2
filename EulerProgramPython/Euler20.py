def Factorial(n):
    if n <= 1:
        return 1
    else: return Factorial(n-1)*n
A = str(Factorial(100))
j = 0
Sum = 0
while j < len(A):
    Sum = Sum + int(A[j])
    j = j+1
print(Sum)