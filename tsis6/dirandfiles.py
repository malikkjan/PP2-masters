#1
import os

def list_directories_files(path):
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return dirs, files

def list_all_directories_files(path):
    all_dirs = []
    all_files = []
    for root, dirs, files in os.walk(path):
        all_dirs.extend(dirs)
        all_files.extend(files)
    return all_dirs, all_files

path = "c:/Users/Малик/Desktop/фин рынки"
directories, files = list_directories_files(path)
print("Directories:", directories)
print("Files:", files)

all_directories, all_files = list_all_directories_files(path)
print("All Directories:", all_directories)
print("All Files:", all_files)

#2
import os

def check_access(path):
    access = {
        "exists": os.path.exists(path),
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK)
    }
    return access

path = "c:/Users/Малик/Desktop/фин рынки"
access_info = check_access(path)
print("Access Information:", access_info)

#3
import os

def path_info(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return filename, directory
    else:
        return "Path does not exist", None

path = "c:/Users/Малик/Desktop/фин рынки"
filename, directory = path_info(path)
print("Filename:", filename)
print("Directory:", directory)

#4
def count_lines(filename):
    with open(filename, 'r') as file:
        return sum(1 for line in file)

filename = "C:/Users/Малик/Desktop/Tor Browser/Browser/TorBrowser/Docs/ChangeLog.txt"
num_lines = count_lines(filename)
print("Number of lines in the file:", num_lines)

#5
def write_list_to_file(lst, filename):
    with open(filename, 'w') as file:
        for item in lst:
            file.write(str(item) + '\n')

my_list = ["apple", "banana", "cherry"]
filename = "C:/Users/Малик/Downloads/gitignore.txt"
write_list_to_file(my_list, filename)

#6
import string

for letter in string.ascii_uppercase:
    with open(letter + ".txt", 'w') as file:
        pass

#7
def copy_file(source, destination):
    with open(source, 'r', encoding='utf-8') as src, open(destination, 'w') as dest:
        dest.write(src.read())

source_file = "C:/Users/Малик/Downloads/row.txt"
destination_file = "C:/Users/Малик/Downloads/gitignore.txt"
copy_file(source_file, destination_file)

#8
import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print("File deleted successfully.")
        else:
            print("No write access to file.")
    else:
        print("File does not exist.")

path = "C:/Users/Малик/Downloads/row (1).txt"
delete_file(path)