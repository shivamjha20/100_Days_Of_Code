'''strip():- The strip() method removes any white spaces before 
and after the string.'''
name="     Shivam     "
print(name.strip())
'''rstrip():- The rstrip() method removes any trailing characters.
'''
a="OP!!!"
print(a.rstrip("!"))
'''replace():- The replace() method replaces all occurances
of a string with another string'''
print(a.replace("!","@"))
'''split():- The split() method splits the given string at the
specified instance and returns the separated string as list
items'''
str1="happy sad"
print(str1.split(" "))