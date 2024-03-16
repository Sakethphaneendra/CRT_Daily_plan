import os,csv
class Home:
    def Products(self):
        self.StudentDetails = open('Products.csv',"a",newline="")
        self.Data = csv.writer(self.StudentDetails)
    def ProductsPage(self):
        os.system('cls')
        print("\n \t\t\t Welcome to Coding Hub Home Page\n\n")

        # Coding Guide Book - 2000 - 20 - books
        i=1
        with open('Products.csv',"r",newline='') as file:
                    reader=csv.DictReader(file)
                    for row in reader:
                        print(i,".Product Name  :",row['ProductName'],"\n   Product Price :",row['ProductPrice'],"\n   Stock Left    :",row['ProductQuantity'],"\n   Product Price :",row['ProductPrice'],"\n   Type          :",row['ProductType'],"\n")
                        i+=1
        while(True):
           
            USP = input("\n\n Enter the Product Name or ProductId here :: ")
            while(True):
                self.Count = int(input(" Enter the Quantity of Product here       :: "))
                if(self.Count>300):print("Sorry, We are out Stock")
                else:break
           
            if USP in ['1', 'Coding is Skill', 'coding is skill']:h.Billing("2999");break
            elif USP in ['2', 'Learn Python', 'learn python']:h.Billing("999");break
            elif USP in ['3', 'SQL Basics', 'sql basics']: h.Billing("199");break
            elif USP in ['4', 'bug & deBug', 'bug and deBug']: h.Billing("299");break
            else: print("  Invalid Option Try Again ")
              
    def Billing(self,PI):
        
            
          os.system('cls')
          print("\n\t\t\t\tBilling System\n\n")
          with open('Products.csv',"r",newline='') as file:
            reader=csv.DictReader(file) 
            for row in reader:
                if (row['ProductPrice']==PI):
                    if(PI=="2999"):bil2=2999*self.Count
                    if(PI=="999"):bil2=999*self.Count
                    if(PI=="199"):bil2=199*self.Count
                    if(PI=="299"):bil2=299*self.Count
                
                    print("   Product Name   :",row['ProductName'],"\n   Product Price  :",bil2,"\n   Mode           : Cash on Delivery\n","\n   Woww Our Order Was Placed Successuly \n")
                    
            print("Enter 'O' to go to Shoping :")
            print("Enter 'x' to Exit CodingHub")   
            saketh = input("\n Enter Here : ")
            if(saketh=='x' or saketh=="X") :
                 os.system('cls')
                 print("\n\n\n\n\t\t\t\t   Thank you\n\n\n\n")
            else:h.ProductsPage()
                 

h=Home()
# h.Products()
h.ProductsPage()
