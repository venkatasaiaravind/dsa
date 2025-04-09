# dsa
DSA 

DAY -> 1

 
					watermelon problem 
A. Watermelon
time limit per test1 second
memory limit per test64 megabytes
One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.

Input
The first (and the only) input line contains integer number w (1 ≤ w ≤ 100) — the weight of the watermelon bought by the boys.

Output
Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.

Examples
InputCopy
8
OutputCopy
YES






code 


w=int(input("enter weight of watermelon :"))
if(w%2!=0 or w<3):
	print("No")
else:
	x=w//2
	if(x%2==0):
		print(x,x)
	else:
		print(x-1,x+1)






					Cheap Travel


Ann has recently started commuting by subway. We know that a one ride subway ticket costs a rubles. Besides, Ann found out that she can buy a special ticket for m rides (she can buy it several times). It costs b rubles. Ann did the math; she will need to use subway n times. Help Ann, tell her what is the minimum sum of money she will have to spend to make n rides?

Input
The single line contains four space-separated integers n, m, a, b (1 ≤ n, m, a, b ≤ 1000) — the number of rides Ann has planned, the number of rides covered by the m ride ticket, the price of a one ride ticket and the price of an m ride ticket.

Output
Print a single integer — the minimum sum in rubles that Ann will need to spend.

Examples
InputCopy
6 2 1 2
OutputCopy
6
InputCopy
5 2 2 3
OutputCopy
8



code

n,m,a,b=map(int,input().split())
if(m*a<b):
    print(n*a)
else:
    print((n//m)*b+min((n%m)*a,b))



					Police Recruits
time limit per test1 second
memory limit per test256 megabytes
The police department of your city has just started its journey. Initially, they don’t have any manpower. So, they started hiring new recruits in groups.

Meanwhile, crimes keeps occurring within the city. One member of the police force can investigate only one crime during his/her lifetime.

If there is no police officer free (isn't busy with crime) during the occurrence of a crime, it will go untreated.

Given the chronological order of crime occurrences and recruit hirings, find the number of crimes which will go untreated.

Input
The first line of input will contain an integer n (1 ≤ n ≤ 105), the number of events. The next line will contain n space-separated integers.

If the integer is -1 then it means a crime has occurred. Otherwise, the integer will be positive, the number of officers recruited together at that time. No more than 10 officers will be recruited at a time.

Output
Print a single integer, the number of crimes which will go untreated.

Examples
InputCopy
3
-1 -1 1
OutputCopy
2
InputCopy
8
1 -1 1 -1 -1 1 1 1
OutputCopy
1
InputCopy
11
-1 -1 2 -1 -1 -1 -1 -1 -1 -1 -1
OutputCopy
8
Note
Lets consider the second example:

Firstly one person is hired.
Then crime appears, the last hired person will investigate this crime.
One more person is hired.
One more crime appears, the last hired person will investigate this crime.
Crime appears. There is no free policeman at the time, so this crime will go untreated.
One more person is hired.
One more person is hired.
One more person is hired.

code 
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

why array index always starts from 0?
  0     1    2     3     4     5    
-------------------------------------
| 10 | 20  | 30 | 40  |  50  | 60  |
-------------------------------------
0x100 0x101 0x108 0x112 0x116 0x120

array elements accessing time complexity 0(1) (because it uses formula) 

FORMULA    BASEADDRESS + (OFFSET*SIZE OF DATATYPE)
EX:-if we want 4th element 
	
	0x100 + (4*4)
	0x100 +16
	0x116 -> this is going to be 5th element.
	so,we need to subtract -1 from the offset 
	0x100 + ((4-1)*4)
	0x100+12
	0x112


DAY -> 2



