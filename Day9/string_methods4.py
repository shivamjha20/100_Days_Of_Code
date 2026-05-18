'''find():- The find() method searches for the first occurence
of the given value and return the index where it is present.
If given value is absent from the string then return -1.'''
str1="He is a good teacher"
print(str1.find("a"))
print(str1.find("to"))

'''index():- The index() method searches for the first occurrence
of the given value and returns the index where it is present.
If the given value is absent from the string then raise an
exception'''
str2="He is a good teacher"
print(str2.index("a"))
#Similar to find() but if value is absent it raises exception.

'''isalnum():- The isalnum() method returns true only if the string
only consists of A-Z,a-z,0-9. If any other character or punctuations 
are present , then it returns false.'''
str2="Welcometohell"
str3="Welcome to hell"
print(str2.isalnum())
print(str3.isalnum())
