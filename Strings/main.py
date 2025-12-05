# single quote
str = "hello from str1"

# double
str2 = 'hello from str2'

# triple
str3 = """hello from str3"""

# escape sequence characters used for formatting like - space, tab
#\n new line
#\t tab
str4 = "this is string 1.\n this is string 2.\t this is string 3"

print (str4)

# concatenation 
str5 = "Suman"
str6 = "devi"

str7 = str5 +" "+ str6
print (str7)

#  string lenght
print (len(str7))

# Indexing 
# we can not manipulate string using index assignment 
strr = "Welcome"

ch = strr[0]
print (ch)
print (strr[4])

# slicing 
string = "Welcome back"

print (string [1:5]) #output =elco
print (string[1 :]) # output = elcome back
print (string [:6]) #welcom

# negative index
string1 = "Suman" # reading string from last elements  
print (string1[-3:-1])

# String Functions 
final_string = "Functions in Python"

print(final_string.endswith("on")) #return true if string ends with the given substring

print (final_string.capitalize()) #capitalize 1st char

print (final_string.replace("Python","python")) # replace all occurrence of old with new 

print (final_string.find("P")) # return 1st index of 1st occurrence & -1 if string does not exist

print (final_string.count("on")) # count the occurrence of substr in string 

