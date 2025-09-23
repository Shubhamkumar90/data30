def usingforloop(n):
    for i in range(1,11):
        print(n*i)

def usingwhileloop(n):
    i=1
    while(i<=10):
        print(n*i)
        i+=1

n=int(input("Enter a number: "))
usingwhileloop(n)