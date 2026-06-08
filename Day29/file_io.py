#Appending to a File.
with open("example.txt", "a") as f:
    f.write("\nThis line was appended.")

#File handling functions
import os
print(os.path.exists("example.txt"))  # Check if file exists
print(os.path.getsize("example.txt")) # File size in bytes

'''tell():-
Returns the current position of the file pointer (in bytes).
Useful for debugging or tracking where you are in the file.'''
with open("example.txt", "r") as f:
    print(f.tell())       # 0 (start of file)
    f.read(5)
    print(f.tell())       # 5 (after reading 5 characters)

