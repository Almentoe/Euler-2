my_set = []
for base in range(2,101):
    for power in range(2,101):
        if base**power not in my_set:
            my_set = my_set + [base**power,]
print(len(my_set))     