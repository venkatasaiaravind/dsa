l=[1,2,4,5,7,2,6,3]
sum = 0
for i in range(len(l)):
    if(i%2!=0):
        sum+=l[i]
print(sum)