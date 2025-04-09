l=[10,20,30,40,30,20,30]
res=[]
for i in l:
    if (l.count(i)%2!=0 and i not in res):
        res.append(i)
print(res)