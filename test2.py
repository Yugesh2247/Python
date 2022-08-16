s1='saiugesh'
s2='selena'
l1=list(s1)
l2=list(s2)
result=[]
for i in l1:
    if i in l2:
        result.append(i)
    else:
        continue
for i in result:
    print(i)
print(len(result))
