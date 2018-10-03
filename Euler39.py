math

Squares = {x**2 for x in range(1,1001)}

Pythagorean_Triples_With_Perimeter = []

for a in range(1,1001):
    for b in range(1,a):
        if a**2 + b**2 in Squares:
            c = int(sqrt(a**2+b**2))
            p = a+b+c
            if p <= 1000:
                Pythagorean_Triples_With_Perimeter += [(a,b,c,p),]
            
#print(Pythagorean_Triples_With_Perimeter)

Pythagorean_Triples_With_Perimeter_Set = {x for x in Pythagorean_Triples_With_Perimeter}

def collect_perimeter(p):
    p_List = []
    for x in Pythagorean_Triples_With_Perimeter_Set:
        if x[3] == p:
            p_List += [x,]
    return len(p_List)

Solutions_number = []
p = 1
while p <= 1000:
    Solutions_number += [(p,collect_perimeter(p)),]
    p += 1
    
print(sorted(Solutions_number, key = lambda x: x[1])[-1])   
# sorted(l, key=lambda x: x[2])    