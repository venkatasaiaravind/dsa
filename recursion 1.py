def fun(n):
    if 1>n:
        return
    print(n,end=" ")
    fun(n-1)
fun(5)