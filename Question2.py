'''Online Vegetable Store
Create a class Vegetable with the below attributes:
name of type String name of the vegetable price of type float //price ( in Rupees ) of the Fx: Kilogram quantity of type int ,/ quantity — number of units / Number of Kilograms
Create the init method which takes all parameters in the above sequence. The method should set the value of attributes with the parameter values received from main function.
Create another class Store with the below attribute: storeName of type String /specifies the vegList of type List L ist of Vegetable which takes all sequence. 
The method should set the value of attributes with the parameter values received from main.
Create method inside the Store class with name categorizeVegetablesAlphabetically
This method use and traverse the list of Vegetables(vegList) and returns a dictionary of alphabetically categorized 
and sorted vegetable names(name), where in key represent an alphabet character(e.g. ‘a’, ‘b’, se etc) 
and value represents a tuple, containing vegetable names that starts with that specific character as per key. 
Both the keys and values are sorted in alphabetically. The comparison needs to be case insensitive. 
If there are more vegetable names starts with the respective alphabet (which is acting as the key for the respective 
tuple of vegetable names), then the list of vegitable names also needs to be sorted.
e.g. Ex on fruits, resultant dictionary data looks like : fas:(‘ananas’, ‘apple), ’13: (‘banana’), ‘p’:(‘pineapple)) Here ‘a’ ,’b’ and 
‘p’ (excluding the single quote ) represents the keys of dictionary and (‘ananass, ‘apple), (‘banana’), (pineapple’) ,excluding the ‘single quote and brackets’ 
represents the tuple for respective and corresponding keys(a , b, p ).
For more details refer the sample test case input and respective output
Create another method inside Store class with the name filterVegetablesForPriceRange 
This method takes minimum price and maximum price in Rupees as input parameters and return a list of alphabetically sorted vegetable names(name), 
where in the Vegetable unit price falls in the given range(minimum price and maximum price). This method use and traverse the list of Vegetables(vegList) 
for comparing the price of vegetable per Unit with the given range
If there is no vegetable in given price range, the method returns an empty list and based on the value main function should print “No Vegetable(s) in the given price range” (Excluding the double quotes) .
For more details refer the sample test case input and respective output
You can use/refer the below given sample input and output to verify your solution using ‘ Custom Input ‘ option ,down the coding editor
Instructions to write main and to call the methods of the classes defined above:
a. You would required to write the main function completely, please follow the below instructions for the same.
b. You would required to write the main program which is inlign to the “sample input description section” mentioned below and to read the data in the same sequence.
c. Create the respective objects(Vegetable and Store) with the given sequence of arguments to fulfill the constructor requirement defined in the respective class.
i.Create a Vegetable object after reading the data related to Vegetable and add the Vegetable object to list of Vegetable objects, This point repeats for the number of 
Vegetable objects you want to create and add to Vegetable list or as mentioned in the first line of input in the input data
ii. Create Store object by passing the Store name and list of Vegetable objects ( created and as mentioned in above point# c.i ) as the arguments to the constructor .
d. Call the methods ( categorizeVegetablesAlphabetically and f ilterVegetablesForPriceRange) mentioned above from the main function in the same order , they appear in the question text. 
e. Display the data returned by the functions , in the main program as per the order of calling the functions and as per the format mentioned in the sample output. f. If None/empty list is returned.
y 1 terVegeta function then display “No Vegetable found for given prince range” (excluding the double quotes) in the main function.
Sample Input (below) description:
• The first input line represents the count of vegetable objects to create and add to the vegetable list.
• Second set of inputs lines(2nd to 4th ) represents vegetable name, vegetable price and quantity of first vegetable object and this set(Name,Price and Quantity for each different vegetable object ) 
of input is repeated for the number of vegetable objects mentioned in the first line of input .
• Next inputs represents store name(third line of input from last).
• Last two lines represents the minimum price and maximum price to be 
supplied to the filterVegetablesForPriceRange to find the vegitables, whose price falls in the range
Sample Testcase Input:
5
corn
20.0
30
onion
10.0
15
potato
30.0
10
cucumber
5.0
10
brocolli
24.5
8
big
bazaar
5.0
25.0
SampleTestcaseOutput:
b
brocolli
c
corn
cucumber
0
onion
P
potato
5.0-25.0
brocolli
corn
cucumber
onion'''




Solution:
class Vegetable:
    def _init_(self,name,price,unit):
        self.name=name
        self.price=price
        self.unit=unit
class Store:
    def _init_(self,storeName,vegList):
        self.storeName=storeName
        self.vegList=vegList
    def createDict(arr):
        arr.sort()
        actual=[]
        d={}
        for i in arr:
            if i[0] not in d:
                d[i[0]]=1
                actual.append(i[0])
                actual.append(i)
            else:
                actual.append(i)
        return actual
                
    def vegInRange(arr,max_price,min_price):
        actual=[]
        for i in arr:
            if i.price<=max_price and i.price>=min_price:
                actual.append(i.name)
        if actual!=[]:        
            actual.sort()
        return(actual)
        
#main_function
my_list=[]
veg=[]
n=int(input())
for i in range(n):
    name=input()
    price=float(input())
    unit=int(input())
    my_list.append(Vegetable(name,price,unit))
    veg.append(name)
storename=input()
obj=Store(storename,veg)
price1=float(input())
price2=float(input())
result1=Store.createDict(veg)
result2=Store.vegInRange(my_list,price2,price1)
for i in result1:
    print(i)
print(str(price1)+'-'+str(price2))
if result2==[]:
    print("No Vegetable(s) in the given range")
else:
    for i in result2:
        print(i)
