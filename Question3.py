'''Take list of employees (id, name and leaves (el, sl, cl).
For a particular employee… Demand a leave from available leave types…
Return available leaves…If available is greater than or equal to demand, 
return ‘Granted’, else ‘Rejected’.
        =>Data wasn't available'''

#Solution:

class Employee:
    def init(self,emp_no,emp_name,leaves):
        self.emp_no=emp_no
        self.emp_name=emp_name
        self.leaves=leaves
class Company:
    def init(self,company_name,emps):
        self.company_name=company_name
        self.emps=emps
    def display_leave(self,emp_no1,Ltype):
        for i in self.emps:
            if i.emp_no==emp_no1:
                return i.leaves[Ltype]
    def Number_of_leaves(self,emp_no1,Ltype,nol):
        for i in self.emps:
            if i.emp_no==emp_no1:
                if i.leaves[Ltype]>=nol:
                    return “Granted”
                else:
                    return “Rejected”
n=int(input())
emps=[]
c=Company(“ABC”,emps)
leaves={}
for i in range(n):
    emp_no=int(input())
    emp_name=input()
    leaves[“CL”]=int(input())
    leaves[“EL”]=int(input())
    leaves[“SL”]=int(input())
    c.emps.append(Employee(emp_no,emp_name,leaves))
emp_no1=int(input())
Ltype=input()
nol=int(input())
print(c.display_leave(emp_no1,Ltype))
print(c.Number_of_leaves(emp_no1,Ltype,nol))
