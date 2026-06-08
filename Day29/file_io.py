#Appending to a File.
with open("example.txt", "a") as f:
    f.write("\nThis line was appended.")

#File handling functions
import os
print(os.path.exists("example.txt"))  # Check if file exists
print(os.path.getsize("example.txt")) # File size in bytes
    
