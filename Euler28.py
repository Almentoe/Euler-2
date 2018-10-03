def sum_numbers_in_perimeter_square(n):
    assert n%2 > 0
    if n == 1:
        return 1
    else:
        return 4*n**2 - 6*(n-1)

grid_sum = 0
n = 1
while n <= 1001:
    grid_sum = grid_sum + sum_numbers_in_perimeter_square(n)
    n = n+2
    
print(grid_sum)   
   
#print(sum_numbers_in_perimeter_square(5))
#print(sum_numbers_in_perimeter_square(3))