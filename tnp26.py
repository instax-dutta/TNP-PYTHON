#approach 3 given by sir 
list=[1,3,2,4,6,1]
max=max(list)
dummy=[max]*len(list)
for i in range(0,len(list)):
    dummy[i]=max-list[i]
for i in range(0,max):
    for j in range(0,len(list)):
        if(dummy[j]>0):
            print(" ",end='')
            dummy[j]-=1
        else:
            print("* ",end='')
    print()