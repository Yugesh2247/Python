st="heelou"
l=['a','A','e','E','i','I','o','O','u','U']
l2=[]
for i in st:
    if i in l:
        l2.append(i)

for i in l2:
    if ((i=='e') or (i=='E')):
        l.replace('e','u')
print(l2)
