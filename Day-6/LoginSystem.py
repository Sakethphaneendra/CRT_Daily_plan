# task : print only ids and names
import csv
class Students:
    def __init__(self):
        self.StudentDetails = open('StudentTable.csv',"a",newline="")
        self.Data = csv.writer(self.StudentDetails)
        self.Data.writerow(["StudentId","StudentName","StudentRoll","StudentBranch"])

    def StudentDetails():
        StudentId = input("Enter Student Id : " )
        StudentName = input("Enter Student Name : " )
        StudentRoll = input("Enter Student Roll Number : " )
        StudentBranch = input("Enter Student Branch : " )
        StudentDetails = open('StudentTable.csv',"a",newline="")
        Data = csv.writer(StudentDetails)
        Data.writerow([StudentId,StudentName,StudentRoll,StudentBranch])
        print("Student Data Stored..")  

    def PrintUserDetail():
        with open('StudentTable.csv',"r",newline='') as file:
            reader=csv.DictReader(file)
            for row in reader:
                print(row['StudentId'] , row['StudentName'])

# Students()
# Students.StudentDetails()
Students.PrintUserDetail()




'''

Create an Ecom Project where user can Register and login him self
Step-2 : Display Products Present = > Products Details Name,Price,Categ and Stock Left
Step-3 : User can Place A Order just by the product name and quatity After Bill should be Genarated with Amount + Order Placed + Pay in Delivery the change of stock should reflected on the Display  

'''