SquareSum = 0
SumSquares = 0
N = 100
i = 0
while i <= N:
    SquareSum = SquareSum + i**2
    i=i + 1
    
j = 0
while j <= N:
    SumSquares = SumSquares + j
    j=j + 1
    
A = SquareSum
B = SumSquares**2

print(B-A)