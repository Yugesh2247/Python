import statistics
n=int(input())
lst=[]
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
print(lst)
lst.sort()
print(lst)
result=statistics.median(lst)
print(result)
