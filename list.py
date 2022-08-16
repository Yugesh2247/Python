list=[1,2,3,'selena']
print(list)
# append:used to insert at last position
list.append('helloselena')
print(list)
#remove  :used to remove a specified element
list.remove('helloselena')
print(list)
#insert: is used to add at specified position
list.insert(0,0)
print(list)
list1=[8,3,4,5]
list1.extend(list)#used to add elements of list into list1
print(list1)
list2=[1,2,3,0,-1]
print(sum(list2))#used to add elements of the list
list2=[1,1,1,1,2,3,3,4,4,5]
print(list2.count(1))# used to count the number elements
# len : used to count the length of the list
print(len(list2))
print(min(list2))
print(max(list2))
list2.sort()
print(list2)
list2.reverse()
print(list2)


# common elements:


l1=[1,2,3,4,5]
l2=[3,4,5,6,7]
l3=[]
l4=[]
for i in l1:
    if i in l2:
        l3.append(i)
    else:
        continue
for i in l2:
    if i in l1:
        l4.append(i)
    else:
        continue
print(l3)
print(l4)


# common ele remove
l5=(l1)
l6=(l2)
for i in l5:
    if i in l6:
        l5.remove(i)
    else:
        continue
for i in l6:
    if i in l5:
        l5.remove(i)
print(l5)



#print elements repeated more than 1 times

le=[1,2,3,1,2,3,4,1,3,6,6,6]
le1=[]
for i in le:
    if le.count(i)>1:
        if i not in le1:
            le1.append(i)
print(le1)



#difference of the elements

a=[1,2,3]
b=[]
for i in range(1,len(a)):
    
    b.append(a[i]-a[i-1])
print(b)


le3=[]
for i in range(1,len(le)):
    le3.append(le[i]-le[i-1])
print(le3)






