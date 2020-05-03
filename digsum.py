t=int(input())

for x in range(t):
    num=int(input())
    sum=0
    while num > 0:
        sum+= num % 10
        num=int(num/10)
        
    print(int(sum))

