'''Given passenger ID name gender distance
In last two lines they provide the passenger ID and discount percentage 
We need to print the discount to be given for that particular passenger  
if that given Id is not in the list print no name or no value
input :
4
101
a
f
10000
102
b
m
12000
103
c
f
45000
104
d
m
65000
101
5
output: 
discount of 101 is: 500.0'''

#Solution:
class Pasanger:
    def _init_(self,id,name,gender,distance):
        self.id=id
        self.name=name
        self.gender=gender
        self.distance=distance
    def discountAmount(obj_list,target_id,discount):
        count=0
        for i in obj_list:
            if i.id==target_id:
                return(i.distance*(discount/100))
            else:
                count+=1
        if count==len(obj_list):
            return None

#main_function
my_list=[]
n=int(input())
for i in range(n):
    id=int(input())
    name=input()
    gender=input()
    distance=int(input())
    my_list.append(Pasanger(id,name,gender,distance))
target=int(input())
discount=int(input())
result=Pasanger.discountAmount(my_list,target,discount)
if result!=None:
    print("discount of %d is: %.1f"%(target,result))
else:
    print("No Value")
