#  open file and read all file 

# f = open("../demo.txt","r")
# file = f.read()
# print(type(file))
# print(file)
# f.close()

#  file read single line 

# f = open("../demo.txt","r")
# file_data = f.read()
# print(file_data)

# print(f.readline())
# print(f.readline())


# open file and write text  overwrite 

# f = open("../demo.txt","w")

# f.write("I wont to learn python tommorow .")
# f.close()

f = open("../demo.txt","a")

f.write(" Them I'll move Node js  \n")
f.close()