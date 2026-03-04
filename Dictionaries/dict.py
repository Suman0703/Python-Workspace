""" Dictionaries are used to store data values in key:value pairs . They are unordered, mutable and don't allow duplicate keys"""

dict = {
    "key":"value",
    "name":"Suman",
    "age":19,
    "course":"B.tech",
    "is_adult":True,
    "subjects":["Math","English","Science"],
    "tuple":(2,3,4,5),
    "marks": 98.8
}

print(dict)
print(type(dict))

print(dict["age"])

# renaming
dict["age"] = 20
print(dict)

# adding new key:value pair
dict["branch"] = "CSE"
print(dict)

# null dic
null_dec = {}

# nested dictionaries

info = {
    "Name":"Suman",
    "marks":{
        "phy":99,
        "math":98,
        "eng":97
    }
}

print(info)

#nested element
print (info ["marks"]["phy"])