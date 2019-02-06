import itertools
# would like to represent all numbers up to 10^10 -1..
# and remove all numbers for which a digit is repeated
position = 1
number = "0123456789"
def CountNumber(String,Number):
    CountOfNumber = 0
    PositionOfCount = 0
    while PositionOfCount < len(String):
        if int(String[PositionOfCount]) == Number:
            
            CountOfNumber = CountOfNumber + 1
            PositionOfCount = PositionOfCount +1
        else:
            PositionOfCount = PositionOfCount +1
            
    return CountOfNumber

def IsDigitRepeated(String):
    j = 0
    DigitSquareSum = 0
    while j < 10:
        DigitSquareSum = DigitSquareSum + (CountNumber(String,j))**2
#        print(DigitSquareSum)
        j = j + 1
    return DigitSquareSum == 10

#NoRepeats = [x for x in range(123456789,9876543211) if IsDigitRepeated(str(x)) == True]
#NoRepeatsSet = {x: x  for x in NoRepeats}
#The above two lines take wayyyy too long to compute.
PermuteList = [str(x) for x in range(10)]
#print(PermuteList)
# want a decision tree set like: (DescisionNumber,NumberChosen)

M =list(itertools.permutations("0123456789"))[(10**6)-1]
print(M)



        
#print(NumberScan)  

#print(IsDigitRepeated("0123456789"))
#print(CountNumber("1234567890",0))
#print("faggot"[4])