n,k = map(int, input().split())
cnt=0
for i in range(n):
    x = int(input())
    if x % k==0:
        cnt=cnt+1

print(cnt)