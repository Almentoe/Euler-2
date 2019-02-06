import math
def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if n%i == 0:
      return False
  return True

textfile = open('mytextfile.txt', 'w')
for i in range(1, 10):
    save =  str(i) 
    textfile.write(save + '\n')
textfile.close()



textfile = open('mytextfile.txt', 'r')
for number in textfile:
    print(int(number) / 4)
    
primes_list = open("primesList.txt","a")
for i in range(1,10):
    prime = str(i)
    primes_list.write(prime + "\n")
primes_list.close()

primes_list = open("primesList.txt","r")

for x in primes_list:
    print(x)
    
primes_list.close()