L=[1,2,3,1,1,3]
count=0
for i in  range(len(L)):
    for j in range(i+1,len(L)):
        if L[i]==L[j]:
            print(i,j)
            count=count+1
print(count)
