s1='Technovert'
s2='Chronology'
l1=list(s1)
l2=list(s2)
result1=[]
result2=[]
for i in l1:
    if i  not in l2:
        result1.append(i)
    else:
        continue
for i in l2:
    if i not in l1:
        result2.append(i)
    else:
        continue
#print(result1)
s3=''.join(result1)
s4=''.join(result2)
for i in result1:
    if i in l1:
        l1.remove(i)
    else:
        continue
for i in result2:
    if i in l2:
        l2.remove(i)
    else:
        continue

print(s3)
print(s4)
print(s3+s4)
