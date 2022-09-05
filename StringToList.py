s = "Geeks"
x = [i for i in s]
print(x)

# Python code to convert string to list character-wise
# Using re.findall method
import re


# Function which uses re.findall method to convert string to list character wise
def Convert(string):
    return re.findall('[a-zA-Z]', string)


# Driver code
str1 = "ABCD"
print("List of character is : ", Convert(str1))


# Python code to convert string to list character-wise
def Convert(string):
    list1 = []
    list1[:0] = string
    return list1


# Driver code
str1 = "ABCD"
print(Convert(str1))


# Python code to convert string to list
def Convert(string):
    li = list(string.split("-"))
    return li


# Driver code
str1 = "Geeks-for-Geeks"
print(Convert(str1))
