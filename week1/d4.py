def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

primes=[]
for i in range(1,101):
    if isprime(i):
        primes.append(i)

with open("primesData.txt","w") as file:
    file.write(str(primes))
print("Saved in file")    