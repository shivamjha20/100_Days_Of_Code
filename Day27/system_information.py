import os

# Number of CPUs
print("CPU count:", os.cpu_count())

# OS type
print("OS name:", os.name)  # 'posix' (Linux/Mac), 'nt' (Windows)
