class Service:
    def __init__(self,serviceId,name,manufacturer,distance,isInsured,minimumPay):
        self.serviceId=serviceId
        self.name=name
        self.manufacturer=manufacturer
        self.distance=distance
        self.isInsured=isInsured
        self.minimumPay=minimumPay


class ServiceCenter:
    def __init__(self,ser_list,dic):
        self.ser_list=ser_list
        self.dic=dic
    def fulfill(self,state,ser_list):
        result=[]
        for i in self.ser_list:
            if i.isInsured =='yes':
                i.minimumPay=1000
            else:
                i.minimumPay=1750
        for i in self.ser_list:
            if i.distance>5000:
                if state in self.dic.values():
                    result.append(i)
        return result
                
                
    
 

 

n=int(input("enter a number:"))
lst=[]
d={}
for i in range(n):
    serviceId=int(input("enter Serid:"))
    name=input("enter name:")
    manufacturer=input("Enter :")
    distance=int(input("Enter distance:"))
    isInsured=input("enter insurance:")
    s=input()
    d[id]=s
    minimumPay=0
    lst.append(Service(serviceId,name,manufacturer,distance,isInsured,minimumPay))

o=ServiceCenter(lst,d)
stateOfRegistration=input()
b=o.fulfill(stateOfRegistration,lst)
for i in b:
    print(i.serviceId,i.name,i.manufacturer,i.minimumPay)
if len(b)==0:
    print("no Cars Found")
