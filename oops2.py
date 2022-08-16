class Medicine:
    def __init__(self,mName,bat,dis,price):
        self.mName=mName
        self.bat=bat
        self.dis=dis
        self.price=price


class Solution:
    @classmethod
    def getPriceByDisease(cls,lst,disease):
        result=[]
        for i in lst:
            if i.dis.lower()==disease.lower():
                result.append(i.price)
        return result
            




n=int(input('enter'))
lst=[]
for i in range(n):
    mName=input('enter Name')
    bat=input('enter batch')
    dis=input('enter dis')
    price=int(input('enter price'))
    lst.append(Medicine(mName,bat,dis,price))


disease=input('enter disease')
ans=Solution.getPriceByDisease(lst,disease)

for i in ans:
    print(i)
