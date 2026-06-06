import os

# List all files in current directory
print(os.listdir("."))

# Create a new folder
os.mkdir("test_folder")

# Rename a file
with open("old.txt", "w") as f:
    f.write("Hello World")
os.rename("old.txt", "new.txt")

# Remove a file
os.remove("new.txt")

# Remove a directory
os.rmdir("test_folder")
