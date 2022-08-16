a=int(input())
l=[]
for i in range(a):
    l.append(input())
l.sort()
n=len(l)
b=int(l[n-1])
c=int(l[n-2])
d=(b+c)
e=d/2
f=int(e)
g=str(f)
print("First Largest is " +l[n-1]+ " second largest is " +l[n-2]+" and average of both is "+ g)
