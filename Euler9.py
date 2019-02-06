N = 1000
for c in range(1,N):
    for b in range(1,N):
        for a in range(1,N):
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                print(a*b*c)
                
# This is Very Very Slow                