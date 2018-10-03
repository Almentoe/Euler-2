#We shall say that an n-digit number is pandigital if it 
#makes use of all the digits 1 to n exactly once; for example,
# the 5-digit number, 15234, is 1 through 5 pandigital.
#
#The product 7254 is unusual, as the identity, 39 × 186 = 7254,
# containing multiplicand, multiplier, and product is 1 through 9
# pandigital.
#
#Find the sum of all products whose multiplicand/multiplier/product
# identity can be written as a 1 through 9 pandigital.
#
#HINT: Some products can be obtained in more than one way so be
# sure to only include it once in your sum.
import itertools
#want a function that writes a number as a list
#want a function that gives me a set of all permutations on 123456789
#want a function that turns a list of number stings (or numbers
#into a number
#print(len(list(itertools.permutations([1,2,3,4,5,6,7,8,9]))))
#list into numbers first:
NINE = [1,2,3,4,5,6,7,8,9]
def list_to_number(List):
    
#    Takes in a list of numbers and outputs a number:
    number = ""
    counter = 0
    while counter < len(List):
        number += str(List[counter])
        counter += 1
    return int(number)

# need to split a list into a list of three lists of length j,k,len(List) - j-k
# AND j+k <= len(List)

def split_list(input_list,first,second):
    assert first + second <= len(input_list)
    return [input_list[:first],input_list[first:first+second],input_list[first+second :]]
    
def product_check(input_lists):
#    must take in 3 lists, and check if the product of the first two numbers
#    is equal to the last number
    first = input_lists[0]
    second = input_lists[1]
    product = input_lists[2]
    first = list_to_number(first)
    second = list_to_number(second)
    product = list_to_number(product)
    return first*second == product

NINEPERMUTE = list(itertools.permutations([1,2,3,4,5,6,7,8,9]))
NINEPERMUTE = [list(x) for x in NINEPERMUTE]
#product_list = []
#for x in NINEPERMUTE:
#    for j in range(2,5):
#        for k in range(1,j):
#            if j+k <= 9 and product_check(split_list(x,j,k)):
#                product_list += [list_to_number(split_list(x,j,k)[2]),]
#print(sorted(product_list))              
#[4396, 5346, 5346, 5796, 5796, 6952, 7254, 7632, 7852]
#print(4396+5346+5796+6952+7254+7632+7852)
#print(list_to_number(NINE))
#print(split_list(NINE,2,3))
#print(NINEPERMUTE)
