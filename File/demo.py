# with open("practice.txt","w") as f:
#     f.write("Hii Everyone")
#     f.write("\nWe are learing  file i/o")
#     f.write("\nuseing Java")
    
    # demo -2 
    
# with open("practice.txt","r") as f:
#     data = f.read()
#     new_data = data.replace("Java","Python")
#     print(new_data) 
    
# with open("practice.txt","w") as f:
#     f.write(new_data)    

# word ="learing"
# with open("practice.txt","r") as f:
#     data = f.read()
#     if (data.find(word) !=-1):
#         print("existing")
#     else:
#         print("not exist")

# demo -3

# def  check_word_file():
#     word = "Python"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if word in data:
#                 print(line_no)
#                 return 
#             line_no+=1
#     return -1            
                         
# check_word_file()       

# demo-4

# with open("practice.txt","r") as f:
#     data = f.read()
#     print(data)
#     num =""
    
#     for i in range(len(data)):
#         if(data[i]==","):
#             print(int(num))
#             num=""
#         else:
#             num+=data[i]


with open("practice.txt","r") as f:
    data = f.read()
    num = data.split(",")
    
    for val in num:
        if int(val)%2==0:
            print("Even Number",val)
        else:
            print("Odd Number")       
        
            