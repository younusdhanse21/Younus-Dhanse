
import os

# Get the current working directory
current_dir = os.getcwd()
print(f"Current Working Directory: {current_dir}") #

# List files and directories in the current directory
items = os.listdir('.')
print("Items in the current directory:", items) #

# Create a new directory
try:
    os.mkdir("new_folder") #
    print("Directory 'new_folder' created.")
except FileExistsError:
    print("Directory 'new_folder' already exists.")

# Execute a shell command
# Use 'ls' on Unix/macOS or 'dir' on Windows
os.system('ls' if os.name != 'nt' else 'dir') #
