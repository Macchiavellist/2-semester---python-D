import os
import shutil
import string


# 1. List directories, files, and both in a specified path
def list_contents(path):
    if not os.path.exists(path):
        return "Path does not exist."

    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    return {"directories": directories, "files": files, "all": os.listdir(path)}


# 2. Check access to a specified path
def check_access(path):
    return {
        "exists": os.path.exists(path),
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK),
    }


# 3. Check if path exists and get filename & directory portion
def path_info(path):
    if os.path.exists(path):
        return {
            "exists": True,
            "directory": os.path.dirname(path),
            "filename": os.path.basename(path),
        }
    return {"exists": False}


# 4. Count the number of lines in a text file
def count_lines(file_path):
    if not os.path.exists(file_path):
        return "File does not exist."

    with open(file_path, "r", encoding="utf-8") as file:
        return sum(1 for line in file)


# 5. Write a list to a file
def write_list_to_file(file_path, data_list):
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines("\n".join(data_list))


# 6. Generate 26 text files (A.txt to Z.txt)
def generate_alphabet_files(directory):
    os.makedirs(directory, exist_ok=True)
    for letter in string.ascii_uppercase:
        with open(os.path.join(directory, f"{letter}.txt"), "w") as file:
            file.write(f"This is file {letter}.txt\n")


# 7. Copy contents of one file to another
def copy_file(source, destination):
    if os.path.exists(source):
        shutil.copy(source, destination)
        return "File copied successfully."
    return "Source file does not exist."


# 8. Delete file with path check
def delete_file(file_path):
    if os.path.exists(file_path) and os.access(file_path, os.W_OK):
        os.remove(file_path)
        return "File deleted successfully."
    return "File does not exist or no permission to delete."
