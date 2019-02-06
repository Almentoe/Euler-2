import fractions

        
#want a remove digit function take in two numbers, and remove the same digit once if they have a digit in common

def digit_in_common(first,second,digit):
    return str(digit) in str(first) and str(digit) in str(second)

def remove_digit(first,second,digit):
    first_string = str(first)
    second_string = str(second)
    if str(digit) in first_string and str(digit) in second_string:
        if first_string[0] == second_string[0]:
            return fractions.Fraction(int(first_string[1]),int(second_string[1]))
        elif first_string[1] == second_string[0]: 
            return fractions.Fraction(int(first_string[0]),int(second_string[1]))
        elif first_string[0] == second_string[1]:
            return fractions.Fraction(int(first_string[1]),int(second_string[0]))
        elif first_string[1] == second_string[1]:
            return fractions.Fraction(int(first_string[0]),int(second_string[0]))
    else: return fractions.Fraction(first,second)   
#print(remove_digit(33,44,3))

Numbers = []
for x in range(11,100):
    if x%10 != 0:
        Numbers += [x,]
MY_LIST = []    
for x in Numbers:
    for y in Numbers:
        for j in range(1,10):
            if digit_in_common(x,y,j) and x != y and fractions.Fraction(x,y) < 1 :
                if remove_digit(x,y,j) == fractions.Fraction(x,y):
                    MY_LIST += [fractions.Fraction(x,y),]
                    
PRODUCT = 1
for x in MY_LIST:
    PRODUCT *= x
print(PRODUCT)
#print(remove_digit(21,12,2))