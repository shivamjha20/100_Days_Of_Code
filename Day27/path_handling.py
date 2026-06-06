import os

path = "example.txt"

# Absolute path
print(os.path.abspath(path))

# Check if file exists
print(os.path.exists(path))

# Split filename and extension
print(os.path.splitext(path))  # ('example', '.txt')

# Join paths safely
print(os.path.join("folder", "subfolder", "file.txt"))
