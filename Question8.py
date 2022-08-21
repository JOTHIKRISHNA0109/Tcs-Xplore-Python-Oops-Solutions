'''Create a class Bill with attributes mobile number and payment bill.
Create another class mobile with attributes service provider, mobile number, data used, payment method.
Service provider maybe airtel or jio. 
Data used is integer values in Gigabytes(GB). 
Payment method maybe paytm,gpay,amazon and so on.
Create a method calculate bill that takes the list of objects and 
calculates the bill and returns the list of objects of class bill with mobile number and payment bill.
The payment is calculated as follows:
1.If the service provider is airtel, the bill is Rs.11 for every 1GB used and if it is jio, 
the bill is Rs.10 for every 1GB used. 
2. If the payment method is paytm there is a cashback of 10% of the total bill 
for airtel users only. The bill is calculated and rounded off after deducing the cashback value.
input:
3(No of objects to be created) 
airtel 
123
16 
paytm 
airtel 
456 
10 
amazon 
jio 
788
10 
paytm 
Output:
(123,158) 
(456,110) 
(789,100)
'''

#Solution:
class Bill:
    def _init_(self,mob_num,pay_bill):
        self.mob_num=mob_num
        self.pay_bill=pay_bill
class Mobile:
    def _init_(self,service,mob_num,data,pay):
        self.service=service
        self.mob_num=mob_num
        self.data=data
        self.pay=pay
    def calculate_bill(arr):
        actual=[]
        for i in arr:
            chumma=[]
            amount=0
            if i.service=='airtel':
                amount=11*(i.data)
            else:
                amount=10*(i.data)
            if i.pay=='paytm' and i.service=='airtel':
                amount-=(amount*0.1)
            chumma.append(i.mob_num)
            chumma.append(int(amount))
            actual.append(tuple(chumma))
        return actual

#main_function
my_list=[]
n=int(input())
for i in range(n):
    service_provider=input()
    mobile_number=int(input())
    data_used=int(input())
    payment=input()
    my_list.append(Mobile(service_provider,mobile_number,data_used,payment))
result=Mobile.calculate_bill(my_list)
for i in result:
    print(i)
