n=int(input())
police = 0
unsolved = 0
event=list(map(int,input().split()))
for e in event:
    if(e == -1):
        if(police>0):
            police-=1
        else:
            unsolved+=1
    else:
        police+=e
print(unsolved)