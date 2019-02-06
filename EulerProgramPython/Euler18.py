A = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
B = A.replace(" ","")
def Triangular(n):
    return int((n*(n+1))/2)
def CoordsB (i,j):
    assert i <=j
    return int(str(B[2*Triangular(j-1):2*Triangular(j)])[2*i-2:2*i])

def DoubleBinarySet(G):
    # takes in a set of of length r binaries, and outputs binaries of length r+1
    NewBinarySet = ()
    for Binary in G:
        NewBinarySet = NewBinarySet + (Binary + (0,) , Binary + (1,))
    return NewBinarySet

def BinarySetIterate(i):
#  gives a set of all binaries of length i-1
    FinalBinarySet = ((),)
    j = i
    while j > 0:
        FinalBinarySet = DoubleBinarySet(FinalBinarySet)
        j = j-1
    return FinalBinarySet
  
print(BinarySetIterate(14))

def DescisionTreeProduct(Binary):
#calculates the sum of the given addition tree of the binary Binary
    Product = CoordsB(1,1)
    i = 1
    j = 1
    while j<= len(Binary):
        i = i + Binary[j-1]
        j = j + 1
        Product = Product+CoordsB(i,j)
    return Product

ProductSet= []
for M in BinarySetIterate(14):
    ProductSet = ProductSet + [DescisionTreeProduct(M),]
#print(sorted(ProductSet)[-1])    
#print(DescisionTreeProduct((1,1))) 
#print(BinarySetIterate(14))
#print(DoubleBinarySet(((),)))
#print(CoordsB(2,2))
#print ((G + (0,),G + (1,)))
#print(B)