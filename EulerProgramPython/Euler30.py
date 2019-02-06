def digit_power_sum(power,number):
    scan_position = 0
    STRING_OF_NUMBER = str(number)
    power_sum = 0
    while scan_position < len(STRING_OF_NUMBER):
        power_sum = power_sum + (int(STRING_OF_NUMBER[scan_position]))**power
        scan_position += 1
    return power_sum

def is_power_sum(power,number):
    return digit_power_sum(power,number) == number

k=2
power_digit_sum = 0
while k < 1000000:
    if is_power_sum(5,k):
        power_digit_sum += k
        k +=1
    else:
        k +=1
print(power_digit_sum)     
    