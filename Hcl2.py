arr=[1,3,1,4,5,6,3,2]
l=[]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]==arr[j]):
            print(arr[j])

for i in range(0,len(arr)):
    print(count(i))



