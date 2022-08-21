'''Create a class Painting with the below attributes:
paintingID: string type
painterName: string type
paintingPrice: int type
painting type: string type
create constructor (_init_ method) which takes all the above attributes in the same sequence.
Method will set the values passed as an argument to the attributes of the Painting object created.
Create a class ShowRoom with the attribute as a list of paintings obtained from the main function.
paintingList: of type List of Painting objects.
Define two methods inside ShowRoom class.
getTotalPaintingPrice: It takes a string representing the painting type as argument, and returns the total painting price of the paintings of the given type from the paintingList of the ShowRoom. If no paintings of the given type is present in the list then the method returns None.
getPainterWithMaxCountOfPaintings: It finds the name of the painter from the paintingList of the ShowRoom who has the highest count of Paintings. If more than one painter has the highest count of paintings, the method returns the name of the painter whose name comes first as per the alphabetical orders(A-Z).
Instructions to write the main function:
a. You would require to write the main section completely. Hence please follow the below instructions for the same.
b. You would require to write the main program which is inline to the “sample input description section” mentioned below and to read the data in the same sequence.
c. Create the respective objects(Painting and ShowRoom) with the given sequence of arguments to fulfill the _init_ method as mentioned in requirements, defined to the respective classes referring to the below instructions.
i) Create a list of Painting objects which will be passes as argument while calling the functions in main. To create the list,
a. Read a number for the count of Painting objects to be created and added to the list.
b. Create a Painting object after reading the data related to it and add the objects to the list to be created. This points repeats for the number of Paintings object to be created(considered in the first line of input) as per point #c.i.a
ii) Create the ShowRoom object by passing the list created in point #c.i
d. Read a value for painting type to be passed as argument to the method getTotalPaintingPrice.
e. Call the method getTotalPaintingPrice by passing the value read in point #d.
f. Call the method getPainterWithMaxCountOfPaintings.
g. Display the value returned by the method getTotalPaintingPrice. If function return None,Then display “Painting not found”(excluding the quotes).
h. Display the value returned by the method getPainterWithMaxCountOfPaintings.
You can use/refer the below-given sample input and output for more details of the format for input and output.
Sample Input description:
a) First line represents the integer value which represents the number of Painting objects.
b) Next lines of input represents one Painting specific data as below one by one in each line.
paintingId
paintingName
paintingPrice
paintingType
c) The points #b repeats for the number of objects mentioned in the point #a.
d) The last line of input is the painting type to be passed as argument to the method getTotalPaintingPrice.
Consider Case Insensitive for this problem statement.
Consider below sample input and output to verify your implementations:
Sample test case 1 : input:
5
101
Raman
50000
portrait
102
kamaal
30000
portrait
103
Raman
25600
modern
104
sumiran
31000
landscape
105
sumiran
50000
Modern
Modern
Sample test case 1: output:
75600
raman
Sample test case 2 : input:
5
101
Raman
50000
portrait
102
kamaal
30000
portrait
103
ankit
25600
modern
104
sumiran
31000
landscape
105
sumiran
50000
Modern
portrait
Sample test case 2 : output:
80000
sumiran'''





Solution:
class Painting:
    def _init_(self,id,name,price,type):
        self.id=id
        self.name=name
        self.price=price
        self.type=type
class Showroom:
    def _init_(self,paintList):
        self.paintList=paintList
    def getTotalPaintingPrice(arr,target):
        amount=0
        for i in arr:
            if i.type==target:
                amount+=i.price
        return amount
    def getPainterWithMaxCountOfPaintings(arr):
        max=0
        actual=[]
        for i in set(arr):
            if arr.count(i)>max:
                max=arr.count(i)
        for i in set(arr):
            if arr.count(i)==max:
                actual.append(i)
        actual.sort()
        if len(actual)!=len(set(arr)):
            return actual[0]
        else:
            return None

#main_function
my_list=[]
name_arr=[]
n=int(input())
for i in range(n):
    id=int(input())
    name=input()
    price=int(input())
    type=input()
    name_arr.append(name)
    my_list.append(Painting(id,name,price,type))
target=input()
obj=Showroom(my_list)
result1=Showroom.getTotalPaintingPrice(my_list,target)
result2=Showroom.getPainterWithMaxCountOfPaintings(name_arr)
print(result1)
print(result2)
