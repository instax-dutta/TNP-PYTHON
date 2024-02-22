n=int(input())
c=0
n=n*(n+1)
for i in range(0,n):
    for j in range(0, i):
        print(" " , end='')
    for k in range (0,n-i):
        print(c,end='')
        c=+1
    c2=max-c+1
    for l in range(0,n-i):
        print(c2,end='')
        c2+=1
    print()