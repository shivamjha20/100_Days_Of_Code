'''istitle():- The istitle() method returns True only if the 
first letter of each word in the string is capitalized,
 otherwise it returns False.'''
str1 = "World Health Organization"
print(str1.istitle())   # Output: True

str2 = "To kill a Mocking bird"
print(str2.istitle())   # Output: False

'''isupper():- The isupper() method returns True if all
characters in the string are uppercase letters.
If there are any lowercase letters, it returns False.'''
str1 = "HELLO WORLD"
print(str1.isupper())        # True

str2 = "Hello World"
print(str2.isupper())        # False

str3 = "12345!"
print(str3.isupper())        # False (no letters at all)

str4 = "WELCOME123"
print(str4.isupper())        # True (numbers are ignored, only letters matter)

'''startswith():- The startswith() method checks if a string 
begins with the specified prefix. It returns True if it does,
 otherwise False.'''

str1 = "Python Programming"
print(str1.startswith("Python"))     # True

str2 = "Python Programming"
print(str2.startswith("program"))    # False

str3 = "Hello World"
print(str3.startswith("He"))         # True

'''swapcase():- The swapcase() method converts uppercase 
letters to lowercase and lowercase letters to uppercase.
It returns a new string with the swapped cases.'''
str1 = "Hello World"
print(str1.swapcase())     # hELLO wORLD

str2 = "PYTHON"
print(str2.swapcase())     # python

str3 = "javaSCRIPT"
print(str3.swapcase())     # JAVAscript
