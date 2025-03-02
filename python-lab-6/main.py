from module2 import (
    list_contents,
    check_access,
    path_info,
    count_lines,
    write_list_to_file,
    generate_alphabet_files,
    copy_file,
    delete_file,
)

# Example usage
test_path = "test_folder"
file_path = "test.txt"

# 1. List directories and files
print(list_contents(""))

# 2. Check access
print(check_access(test_path))

# 3. Path information
print(path_info(file_path))

# 4. Count lines in a file
print(count_lines(file_path))

# 5. Write list to file
write_list_to_file("output.txt", ["Hello", "World", "Python"])

# 6. Generate A.txt to Z.txt
generate_alphabet_files("alphabet_files")

# 7. Copy file
print(copy_file("output.txt", "copy_output.txt"))

# 8. Delete file
print(delete_file("copy_output.txt"))