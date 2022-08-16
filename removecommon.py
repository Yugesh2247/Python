s1='Technovert'
s2='chronology'
l1=list(s1)
l2=list(s2)
l3=l1.copy()
l4=l2.copy()
print(l1,l2,l3,l4)
for i in l1:
    if i in l2:
        print(i)
        l1.remove(i)
for i in l4:
    if i in l3:
        l4.remove(i)
    else:
        continue
s3=''.join(l1)
s4=''.join(l4)
print(s3,s4)
    
