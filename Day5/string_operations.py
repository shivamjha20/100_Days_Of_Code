# Length of a String
fruit= "apple"
len1=len(fruit)
print("Apple is a ",len1," letter word")

# String As an Array
'''A string is essentially a sequence of characters also called
 an array. Thus we can access the elements of this array'''
name="shivam"
print(name[:6])
print(name[5])

# String slicing
''' The method of specifying the start and the end index to specify
a part of a string is called slicing'''
name="saif"
print(name[:5]) # Slicing from start
print(name[5:]) # Slicing till end
print(name[2:5]) # Slicing in between
print(name[-3:]) # Slicing using negative index
