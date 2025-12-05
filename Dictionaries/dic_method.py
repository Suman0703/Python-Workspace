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

# dictionay methods

print(dict.keys()) #returns all keys
print(list(dict.keys())) #typecasting into list
print(len(dict)) # total no. of keys

print(dict.values()) #return all values

print(dict.items()) #return all key:val pairs

print(dict.get("age")) #returns the values according to the key this method does not give error if key is not found

dict.update({"city":"Hoshiarpur"}) #insert the specified items to the dictionary
print(dict)

dict.update({"city":"Hoshiarpur","village":"none"})