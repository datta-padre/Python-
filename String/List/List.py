# student = ["Akshay",89,"Vishal",201]
# student[0]="Datta"
# print(student)

# mark = [1,2,3,4,5,6,7,8,9]
# print(mark[1:])


list = [2,4,2,6,9]

# Append List 
newlist = list.append(12);

print("Append add on element at the end : ",list)

# sort list 

list.sort();

# sort and revers list 

list.sort(reverse=True)
print("sort the list and revers list :",list)

#  revers list in python

list.reverse()
print("revers in the List",list)

# Insert in the List 

list.insert(0,100)
print("Insert in the first ",list)

# Remove list 

list.remove(100)
print("Remove 100 Values",list)

# Remove Element at Index

list.pop(1)
print(list)