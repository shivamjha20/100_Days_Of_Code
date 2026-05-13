print("Strings\n")
name="shivam"
friend="saif"
print(name,"\n")
'''
Strings:- In python anything that you enclose between single
or double quotation mark is considered as string. A string is
essentially a sequence or array of textual data. Strings are
used when working with unicode characters.'''

# Multiline Strings
print("Multiline Strings")
a='''
In Python, multiline strings are created by wrapping text
in triple quotes—either  single or  double—allowing you
to span multiple lines without needing manual escape characters
like \n.'''
print(a)

# Accessing characters of a string
print("Accessing characters of a string")
print(name[0])
print(name[1],"\n")

# Looping through the string
for character in name:
    print(character)