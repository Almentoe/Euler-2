get_bin = lambda x: format(x, 'b')
DOUBLE_PALINDROME = []
j=1
while j < 1000000:
    if str(j) == str(j)[::-1] and get_bin(j) == get_bin(j)[::-1] and j%2 >0:
        DOUBLE_PALINDROME += [j,]
        j += 1
    else:
        j += 1
print(sum(DOUBLE_PALINDROME))        
print(get_bin(4))
print(get_bin(4)[::-1])
print(get_bin(4)[0])