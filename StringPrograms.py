#   String Programs:
#    _____________________
# 1.  string reverse using slice
s="selena"
output=s[::-1]
print(output)
print("____________")


# 2.String reverse using reversed method:

s='selena'
a=reversed(s)
for i in a:
    print(i,end='')
print()
print("____________")


# 3. String reverse withot using slice,reversed method
print()
s=input("enter some text to reverse:")
output=""
i=len(s)-1
while i>=0:
    output=output+s[i]
    i=i-1
print(output)
print("____________")



# 4. String Reverse order of strings:

s="Learning python is very easy"
a=s.split()
l=a[::-1]
l1=' '.join(l)
print(l1)
print("____________")

# 5. String reverse every second word:


s1="one two three four five"    #output: one owt three rouf five
a1=s1.split()
i=0
l2=[]
while i<len(a1):
    if i%2==0:
        l2.append(a1[i])
    else:
        l2.append(a1[i][::-1]) 
    i=i+1
l3=' '.join(l2)
print(l3)


print("____________")

# 6.print characters present at even and odd seperately

s="selenagomez"
print("characters at odd indexs")
i=0
while i<len(s):
    print(s[i],end="")
    i=i+2
print()
print("characters at even index")
i=1
while i<len(s):
    print(s[i],end="")
    i=i+2
print()
print("____________")

# 6.1 print char present at even and odd seperately using slice

s="selenagomez"
print("characters at odd index:",s[::2])
print("characters at even index:",s[1::2])
print("____________")

# 7.Assume the string contains only alphabets symbols and digits.write a program
   #to sort characters of the string ,first alphabets and followed by digits

s="B4A1D3"
alphabets=[]
digits=[]
for i in s:
    if i.isalpha():
        alphabets.append(i)
    else:
        digits.append(i)

output=''.join((sorted(alphabets)+sorted(digits)))
print(output)
print()
print("____________")


#8.write a program for the following requirements:
#input:a4b3c2
#output:aaaabbbcc

s="a4b3c2"
output=''
for i in s:
    if i.isalpha():
        x=i
    else:
        d=int(i)
        output=output+x*d
print(output)
print()
print("____________")


# 9.write a program findthenumber of oocurance of each character
#input:abcabdabbcde
#output:a-3,b-4,c-3,d-1,e-1

s="ABCABCABBCDE"
d={}
for x in s:
    if x in d.keys():
        d[x]=d[x]+1
    else:
        d[x]=1
for k,v in d.items():
    print("{}-{}".format(k,v),end='')
        

    
