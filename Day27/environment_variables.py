import os

# Get environment variable
print(os.getenv("PATH"))

# Set environment variable
os.environ["MY_VAR"] = "Hello"
print(os.environ["MY_VAR"])
