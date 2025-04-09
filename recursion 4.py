def fun(n,i=1):
    if i>n:
        return
    print(i,end=" ")
    fun(n, )
    if i!=n:
        print(i,end=" ")
fun(5)