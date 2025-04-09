def fun(n):
    if n==0:
        return 200
    print(n,end=" ")
    t=fun(n-1)
    return t
a = 5
print(fun(a))