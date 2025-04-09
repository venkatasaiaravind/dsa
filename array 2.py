#print the list after deleting the duplicate elements in it 
l = list(map(int,input().split()))
l= list(set(l))
print(l)

#or 

a=[10,20,30,40,50,60,10,20,30,40]
res=[]
for i in a:
    if (i not in res):
        res.append(i)
print(res)