'''Create a class employee with attributes
  emp Id,
  emp name,
  emp role,
  emp salary
In the same class,define method increment_salary() which takes number as an argument, 
here number represents the percentage by which the salary should be incremented.
Create another class organization with attributes org_name and list of employee objects
In the same class create a method calculate_salary() which takes string and 
number as the input arguments.string input represents the employee role and 
number represents the percentage by which the salary should be incremented,
return list of employee objects whose salary has incremented.
Note: use increment_salary method in this method
Input:
4
100
rajesh
developer
40000
101
ayesha
developer
41000
102
hari
analyst
45000
103
amar
manager
60000
developer
5
Output:
rajesh
42000.0
ayesha
43050.0
'''
#Solution:
class Employee:
    def _init_(self,id,name,role,salary):
        self.id=id
        self.name=name
        self.role=role
        self.salary=salary
    def increment_salary(arr,num):
        for i in arr:
            i.salary+=((num/100)*i.salary)
class organization:
    def calculate_salary(arr,s,n):
        actual=[]
        for i in arr:
            if i.role==s:
                actual.append(i.name)
                actual.append(i.salary)
        return actual

#main_function
my_list=[]
n=int(input())
for i in range(n):
    id=int(input())
    name=input()
    role=input()
    salary=int(input())
    my_list.append(Employee(id,name,role,salary))
target1=input()
target2=int(input())
Employee.increment_salary(my_list,target2)
result=organization.calculate_salary(my_list,target1,target2)
for i in result:
    print(i)
