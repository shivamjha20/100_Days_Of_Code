#Opening File
file = open("example.txt", "r")  # "r" = read mode
'''Modes:
"r" → read (default)
"w" → write (creates/overwrites file)
"a" → append (adds to end of file)
"x" → create (fails if file exists)
"b" → binary mode (e.g., images)
"t" → text mode (default)'''

# Write text to a file
with open("example.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("This is a second line.")
#Using "with" ensures the file closes automatically.

# Read entire file
with open("example.txt", "r") as f:
    content = f.read()
    print(content)

# Read line by line
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())

# Read into a list
with open("example.txt", "r") as f:
    lines = f.readlines()
    print(lines)
