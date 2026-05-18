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
print(str2.index("to"))#Similar to find() but if value is absent it raises exception.