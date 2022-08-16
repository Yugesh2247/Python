numbers=[1,2,3,4,5,6,7,8,8,8,8,8,8,1,2,3,4,5,6,7,8,9]
l2=[]
l3=[]
for i in numbers:
    if numbers.count(i)>1:
        if i not in l2:
            l2.append(i)
print(len(l2))

