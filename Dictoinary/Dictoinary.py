# dict = {
#     "fullName":{
#         "firstName":"datta",
#         "lastName":"padre"
#     },
#     "subjects":["math","chem","hindhi","marathi"],
#     "email":"dattapadre357@gmail.com"
# }

# print(type(dict))
# print(dict["fullName"]["firstName"])

# dict["subjects"].append("Datta")
# print(dict["subjects"])



#  Dictionary Methods 

# student={
#     "name":"datta",
#     "email":"dattapadre357@gmail.com",
#     "subject":{
#         "math":12,
#         "chem":39,
#         "marathi":59
#     },
#     "password":"Datta@7249"
# }


# print(type(student))
# print(student.keys())   # return all keys in not sub keys  dictinary 
# print(student.values()) # return all values with sub values 

# print("return list:",list(student.values()))
# print("return length:",len(list(student.values())))


student={
    "name":"datta",
    "email":"dattapadre357@gmail.com",
    "subject":{
        "math":12,
        "chem":39,
        "marathi":59
    },
    "password":"Datta@7249"
}

# print(list(student.items()))

print(student.get("email"))

new_dict = {
    "city":"Ahilyanagar"
}

student.update(new_dict)
print(student)