'''Create a class Stock having attributes StockName,StockSector,StockValue. 
Create a method getStockList with takes a list of Stock objects and a StockSector(string) and 
returns a list containing stocks of the given sector having value more than 500.
input:
3
TCS
IT
1000
INFY
IT
400
BMW
Auto
1200
IT
Output:
TCS'''

#Solution:

class Stock:
    def _init_(self,n,s,v):
        self.name=name
        self.sector=sector
        self.value=value
    def getStockList(stocklist,target):
        actual=[]
        for i in stocklist:
            if i.sector==target:
                if i.value>500:
                    actual.append(i.name)
        return actual
#main_function
my_list=[]
n=int(input())
for i in range(n):
    name=input()
    sector=input()
    value=int(input())
    my_list.append(Stock(name,sector,value))
target=input()
result=Stock.getStockList(my_list,target)
for i in result:
    print(i)
