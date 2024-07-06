import os

# Directory containing the text files
directory_path = 'PATH TO/copticmt/CoPARA/copcnt_readaloud'

def count_lines_in_files(directory):
    total_lines = 0
    # Loop through each file in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # Check if it's a file
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                num_lines = sum(1 for line in file)
                total_lines += num_lines
    return total_lines

# Call the function and print the result
total_line_count = count_lines_in_files(directory_path)
print(f"The total number of lines in all files is: {total_line_count}")
