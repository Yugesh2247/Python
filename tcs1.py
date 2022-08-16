lst=['a','e','i','o','u','A','E','I','O','U']
a=int(input())
b=input()
l=[]
count=0
for i in range(a):
    l.append(input())
for i in l:
    k=list(i)
    res=k.count(b)
    for j in k:
        if j in lst:
            s=k.index(j)
            k[s]=b
            count=count+1
        else:
            continue
    count=count+res
    result=''.join(k)
    print(result,count)
    result=''
    count=0
