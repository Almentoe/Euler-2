seed = 1
MIN_FINAL_DIGIT = 10000001
champernowne = ""
while seed > 0:
    if len(champernowne) <= MIN_FINAL_DIGIT:
        champernowne += str(seed)
        seed += 1
    else:
        seed = -1

champernowne_product = 1

j = 0

while j < 7:
    champernowne_product *= int(champernowne[-1 + 10**j])
    j += 1
    
    
print(champernowne_product)
    
        
    
    