import re
c=input()
num1=''
num2=0
l=re.split('[0-9]',c)
l1=re.split('[a-z]',c)
for i in l:
    if i=='':
        l.remove(i)
    else:
         num1+=i         
for i in l1:
    if i=='':
        l1.remove(i)
    else:
        num2+=int(i)
print(num1,num2)        
         
         
