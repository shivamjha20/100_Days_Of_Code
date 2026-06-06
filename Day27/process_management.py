import os

# Run a shell command
os.system("echo Hello World")

# Get process IDs
print("Current PID:", os.getpid())
print("Parent PID:", os.getppid())
