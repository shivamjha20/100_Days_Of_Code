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
