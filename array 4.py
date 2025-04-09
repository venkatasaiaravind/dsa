l=[1,2,3,4,5,6,7,8]

res=[]
l.sort()
for i in l:
    if(i%2==0):
        res.insert(0,i)
    else:
        res.append(i)
print(res)