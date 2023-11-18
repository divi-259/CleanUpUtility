import os
import shutil

# Set a default path to current directory
default_path = os.getcwd()

# Give the complete Directory Path where you want to run the script
user_input = input("Enter folder path: ")
folder_path = user_input if user_input else default_path

# List all files and folders in the directory
contents = os.listdir(folder_path)

# Separate files and folders
files = [f for f in contents if os.path.isfile(os.path.join(folder_path, f))]
folders = [d for d in contents if os.path.isdir(os.path.join(folder_path, d))]

# Delete all image files
print("Files:")
for file in files:
    root, extension = os.path.splitext(file)
    ext = extension.lower();
    #Update the ext variable below to delete the specific kind of files you want to delete
    if ext =='.png' or ext=='.jpg' or ext == '.jpeg' or ext=='.gif' or ext=='.svg' or ext=='ico':
        filepath = os.path.join(folder_path, file)
        print("Deleting File: ", file)
        os.remove(filepath)

# Delete all empty folders
for dir in folders:
    dir_path = os.path.join(folder_path, dir)
    contents = os.listdir(dir_path)
    if len(contents)==0:
        print("Removing Empty folder: ", dir_path)
        shutil.rmtree(dir_path)