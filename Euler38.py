import Euler32

def number_to_list(Number):
    LIST = []
    index = 0
    Number = str(Number)
    while index < len(Number):
        LIST += [int(Number[index])]
        index += 1
    return LIST

def list_to_number(List):
    
#    Takes in a list of numbers and outputs a number:
    number = ""
    counter = 0
    while counter < len(List):
        number += str(List[counter])
        counter += 1
    return int(number)

L = NINEPERMUTE

def mult_stack(Number):
    Stack = []
    String = ""
    j = 1
    while j:
        if len(Stack) < 9:
            Stack += number_to_list(Number*j)
            j += 1
        else:
            break
    return Stack  

def is_stack_permutation(Number):
    return mult_stack(Number) in L
PERMLIST = []
number = 1
while number < 10000:
    if is_stack_permutation(number):
        PERMLIST += [list_to_number(mult_stack(number)),]
        number +=1
    else:
        number +=1
        
print(max(PERMLIST))      
    
# produces str(Number * 1) + str(Number*2)...str(Number*n)
# such that len of the above string is <= 9
