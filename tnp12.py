n=int(input())
list=" "
for i in range(0,n):
    a=int(input())
    list.append(a)

i=0
j=n-1
while i<j:
    list[i],list[j]=list[j],list[i]
    i+=1
    j-=1
print(list)
