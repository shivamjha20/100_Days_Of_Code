'''capitalize():- The capitalize() method turns only the first 
character of the string to uppercase and the rest other character
of the string are turned to lowercase. The string has no effect if 
the first character is already uppercase.'''
str="hello"
print(str.capitalize())
str2="hello World"
print(str2.capitalize())

'''centre:- The centre() method align the string to the centre
as per the parameters given by the user.'''
str3="Welcome to the console"
print(str3.center(50))
print(str3.center(50,"."))
''''''
''''count():- The count() method returns the number of times the 
given value has occured within the given string.'''
str4="London"
print(str4.count("o"))