'''isalpha():- The isalnum() method returns true only if the 
entire string only consists of A-Z,a-z. If any other 
character or punctuations or numbers(0-9) are present , 
then it returns false.'''
str1="welcome"
str2="welcome!!"
print(str1.isalpha())
print(str2.isalpha())

'''islower():- The islower() method returns true if all 
the characters in the string are lower case.'''
str3="hello world"
print(str3.islower())

'''isprintable():- The isprintable() method returns true if 
all the values within the given string are printable, if not
then return false.'''
str4="Happy Diwali All"
str5="Happy Dusherra\n"
print(str4.isprintable())
print(str5.isprintable())

'''isspace():- The isspace() methods return true only and
only if the strings contains white space , else return
false'''
str6="      "       # Using Spacebar 
str7="          "   # Using Tab
print(str6.isspace())
print(str7.isspace())