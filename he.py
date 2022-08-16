numbers=[12,3,4,5,3,3,52,1,7]
l2=[]
for i in numbers:
        if numbers.count(i)>1:
           if i not in l2: 
            l2.append(i)
print(l2)
l3=''.join(l2)
print(l3)

            
