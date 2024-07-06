# # Path to your input file
# input_file_path = 'PATH TO/copticmt/CoPARA/combined_arabic.txt'

# # Path for the output file that will contain no duplicates
# output_file_path = 'PATH TO/copticmt/CoPARA/processed_arabic.txt'

# def remove_duplicates(input_path, output_path):
#     seen_lines = set()
#     with open(input_path, 'r', encoding='utf-8') as file:
#         lines = file.readlines()

#     with open(output_path, 'w', encoding='utf-8') as file:
#         for line in lines:
#             if line not in seen_lines:
#                 file.write(line)
#                 seen_lines.add(line)

# # Call the function with your file paths
# remove_duplicates(input_file_path, output_file_path)
# Path to your Arabic input file
arabic_file_path = 'PATH TO/copticmt/CoPARA/combined_arabic.txt'

# Path to your Coptic input file
coptic_file_path = 'PATH TO/copticmt/CoPARA/combined_coptic.txt'

# Output paths for the files with duplicates removed
output_arabic_file_path = 'PATH TO/copticmt/CoPARA/processed_arabic.txt'
output_coptic_file_path = 'PATH TO/copticmt/CoPARA/processed_coptic.txt'

def remove_parallel_duplicates(arabic_path, coptic_path, output_arabic_path, output_coptic_path):
    seen_lines = set()
    with open(arabic_path, 'r', encoding='utf-8') as arabic_file, open(coptic_path, 'r', encoding='utf-8') as coptic_file:
        arabic_lines = arabic_file.readlines()
        coptic_lines = coptic_file.readlines()

    with open(output_arabic_path, 'w', encoding='utf-8') as out_arabic_file, open(output_coptic_path, 'w', encoding='utf-8') as out_coptic_file:
        for arabic_line, coptic_line in zip(arabic_lines, coptic_lines):
            if arabic_line not in seen_lines:
                out_arabic_file.write(arabic_line)
                out_coptic_file.write(coptic_line)
                seen_lines.add(arabic_line)

# Call the function with your file paths
remove_parallel_duplicates(arabic_file_path, coptic_file_path, output_arabic_file_path, output_coptic_file_path)
