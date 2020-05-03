alist=[]
t=int(input())
for i in range(t):
    x=int(input())
    alist.append(x)

alist.sort()
for i in range(t):
    print(alist[i])

