n=int(input())
list=" "
for i in range(0,n):
    a=int(input())
    list.append(a)
r=int(input())
while(r>0):
    t=list[n-1]
    for i in range(n-1,0,-1):
        list[i]=list[i-1]
    list[0]=t
    r-=1
    print(list)
