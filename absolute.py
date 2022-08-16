s=input("Enter:")
l=s.split(' ')
l1=[]
for i in range(len(l)):
    l1.append(len(l[i]))
print(l1)
for i in l1:
    if i%2==0:
        even=i
        if i>even:
            even=i
for i in range(len(l)):
    if even==len(l[i]):
        print(l[i])
