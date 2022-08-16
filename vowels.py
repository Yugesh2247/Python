from itertools import count


vowels=['a','e','i','o','u','A','E','I','O','U']
n=input("enter your name to find  to count n0.of vowels")
l=list(n)
count=0
l2=[]
for i in l:
    if i in vowels:
        l2.append(i)
s=''.join(l2)
print("vowels are:",s)