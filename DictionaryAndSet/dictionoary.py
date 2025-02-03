#dictionary are used to store data values in key : value pairs
#they are unordered,mutuable(changeable) & don't allow duplicate keys

info = {
    "name" : "Tanish",
    "subjects" : ["OS","CN","Python","Maths"],
    "learning" : "Python",
    "age" : 19,
    "isAdult" : True
}

# print(info)
print(info["name"])#accessing singe value
print(info["subjects"])
print(info["learning"])
print(info.values())#accessing all values



info["name"] = "Akshat"
info["surname"] = "Jain"
print(info["name"],info["surname"])

#null dictionary:
null_dic = {}