# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
        
#     def Avg(self):
#         sum = 0
#         for i in self.marks:
#             sum+=i
#         print("Avrage Marks =",sum/len(self.marks))    
             
# s1 = Student("Datta Padre",[12,21,32])  
# s1.Avg()  


# demo-2


class Account:
    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no
        
    def debit(self,amount):
        print("Debit Amount =",amount," Avlibalce = ",self.balance-amount,"Rs")
        
    def credit(self,amount):
        print("Credit Amount =",amount," Avlibalce = ",self.balance+amount,"Rs")   
        
a1 = Account(1000,43334390070)     

# a1.debit(100)  
a1.credit(100)
                