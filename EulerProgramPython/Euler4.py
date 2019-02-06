x= 'hello world'[::-1]
PalindomeProducts = ()
for a in range(100,999):
    for b in range(100,999):
        
            A = str(a*b)
            B = str(a*b)[::-1]
            if A == B and a <= b:
                
                PalindomeProducts = PalindomeProducts + (a*b,)
#print(PalindomeProducts)
print(sorted(PalindomeProducts)[-1])
        
        
        
        
        
        # PalindomeProducts = PalindomeProducts + (a*b,)