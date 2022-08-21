'''Create a class Doctor with below attributes:
doctorId – Numeric type
doctorName – String type
specialization – String type
consultationFee – Numeric type
doctorId represents the unique identification number of a Doctor object.
doctorName represents the name of the doctor.
specialization represents the doctor specialization and consultationFee represents the doctors fee.
Define the _init_ method to initialize the attributes in the above sequence.
Create a class Hospital with below attribute:
doctorDB   – is of type dictionary with Doctor objects [ Serial number of a Doctor in the Hospital
and the respective Doctor object as a key : value pair ]
Define the _init_ method to initialize the dictionary attribute in the Hospital class . 
It initializes the dictionary of Doctor objects in the Hospital class with the dictionary 
supplied from main program while creating the Hospital object.
The Dictionary( with Doctor serial number and the respective Doctor object as key : value pair ) is created 
and filled in main program by adding each Doctor object. 
This Doctor object is created with the input data related to a respective Doctor object . 
This dictionary after filling to be passed as an argument to the Hospital constructor 
and this will be initialized to doctorDB dictionary with in the Hospital class.
Define two methods – searchByDoctorName and calculateConsultationFeeBySpecialization in Hospital class.
searchByDoctorName:
This method will take Doctor name as a parameter, find the respective Doctor object based on the doctor name given and
return to main function with a list of Doctor objects, whose name matches with the given name, 
supplied as an argument.
If there is no Doctor found with the given name then return None to main program and 
display the message “No Doctor Exists with the given DoctorName” in the main function.
Hint
a. Use the dictionary, doctorDB in hospital to get the consultation fee of each of Doctor (Doctor object in the Hospital ) 
for the given specialization supplied as argument .
b.Display the Total Fee in the  in the main function  – Refer sample testcase below for more details
Instructions to implement Main function:
a. You would required to write the main program completely, hence please follow the below instructions for the same.
b. You would required to write the main program, inlign to the sample input data mentioned below and to read the same  .
c. Create the respective objects(Doctor and Hospital) 
  i.Create a Doctor object after reading the data related to one Doctor and add the doctor object to Doctors dictionary 
  with Serial number and Doctor object as key:value pair.
  ii.Repeat above point for the total number of Doctor objects , read in the first line of input data.
  iii. Create a Hospital Object with the dictionary of Doctor objects, created in the previous step (c.i)
d. Call the methods ( searchByDoctorName and calculateConsultationFeeBySpecialization) mentioned above in the same order , 
    they appear in the question text from main function .
e. Display the data returned by the functions , in the main program as per the format mentioned in the sample output.
    If no Doctor exists with the given name(return value None from the respective function )then display the message “No Doctor Exists with the given DoctorName” in the main function, excluding the double quotes.
    If no Doctor exists with the given specialization (return value 0 from the respective function )then display the message “No Doctor with the given specialization” in the main function, excluding the double quotes.
Sample Input (below) data description:
1.The 1st input taken in the main section is the number of Doctor objects to be created and added to the dictionary of Doctors in the Main program
2.The next set of inputs are the doctorId, doctorName, specialization and consultationFee of first Doctor
3. For each Doctor object repeat point#2  and this point is repeated for number of Doctor objects given in the first line of input
4.The last but one line of input refers the doctorName to be searched  ie an argument for searchByDoctorName function
5. Last line of input represents the specialization, supplied as an argument to calculateConsultationFeeBySpecialization function, 
to get the total consultationFee of all the Doctors for a given specialization.
Sample Input :
5
90901
GovindRajulu
ENT
500
90902
Madhuri
Dermatologist
700
90903
Divya
Gynaecologist
600
90904
Suryam
Cardiologist
900
90905
Madhuri
Cardiologist
1000
Madhuri
Cardiologist
Output :
90902
Madhuri
Dermatologist
700
90905
Madhuri
Cardiologist
1000
1900'''

#Solution:
class Doctor:
    def _init_(self,id,name,spl,fee):
        self.id=id
        self.name=name
        self.spl=spl
        self.fee=fee
class Hospital:
    def _init_(self,doctorDB):
        self.doctorDB=doctorDB
    def searchByDoctorName(arr,target1):
        actual=[]
        for i in arr:
            if i.name==target1:
                actual.append(i.id)
                actual.append(i.name)
                actual.append(i.spl)
                actual.append(i.fee)
        return actual
    def calculateConsultationFeeBySpecialization(arr,target2):
        amount=0
        for i in arr:
            if i.spl==target2:
                amount+=i.fee
        return amount
#main_function
my_list=[]
my_dict={}
n=int(input())
for i in range(n):
    id=int(input())
    name=input()
    spl=input()
    fee=int(input())
    my_list.append(Doctor(id,name,spl,fee))
target1=input()
target2=input()
for i in range(0,len(my_list)-1):
    my_dict[i]=my_list[i]
h=Hospital(my_dict)
result1=Hospital.searchByDoctorName(my_list,target1)
result2=Hospital.calculateConsultationFeeBySpecialization(my_list,target2)
for i in result1:
    print(i)
print(result2)
