import os
import shutil

# Paths to the directories containing the files
arabic_folder = 'PATH TO/CoPARA/arbnav_readaloud'
coptic_folder = 'PATH TO/CoPARA/copcnt_readaloud'
mismatch_arabic_folder = 'PATH TO/CoPARA/mismatchArabic2'
mismatch_coptic_folder = 'PATH TO/CoPARA/mismatchCoptic2'

# Ensure mismatch folders exist
os.makedirs(mismatch_arabic_folder, exist_ok=True)
os.makedirs(mismatch_coptic_folder, exist_ok=True)

# Files for storing combined content of matched files
combined_arabic_file = 'PATH TO/CoPARA/combined_arabic2.txt'
combined_coptic_file = 'PATH TO/CoPARA/combined_coptic2.txt'

# Counters for file processing
total_files = 0
parallel_files = 0
files_with_issues = 0

# Open combined files in append mode
with open(combined_arabic_file, 'a', encoding='utf-8') as arabic_output, \
     open(combined_coptic_file, 'a', encoding='utf-8') as coptic_output:

    # List files in both directories
    arabic_files = {f for f in os.listdir(arabic_folder) if f.endswith('.txt')}
    coptic_files = {f for f in os.listdir(coptic_folder) if f.endswith('.txt')}

    # Total files
    total_files = len(coptic_files)  # assuming we're focusing on Coptic files as the reference

    # Process each Coptic file
    for cop_file in coptic_files:
        # Construct the corresponding Arabic file name using parts for full book number, name, and chapter
        parts = cop_file.split('_')
        if len(parts) >= 4:
            arb_file = f'arbnav_{parts[1]}_{parts[2]}_{parts[3]}_read.txt'
        else:
            continue  # Skip files that do not match the expected pattern

        # Check if the corresponding Arabic file exists
        if arb_file in arabic_files:
            parallel_files += 1
            # Read contents and count lines
            with open(os.path.join(coptic_folder, cop_file), 'r', encoding='utf-8') as file1:
                coptic_content = file1.readlines()

            with open(os.path.join(arabic_folder, arb_file), 'r', encoding='utf-8') as file2:
                arabic_content = file2.readlines()

            # Check if they have the same number of lines
            if len(coptic_content) == len(arabic_content):
                # Write contents to combined files
                arabic_output.writelines(arabic_content)
                coptic_output.writelines(coptic_content)
            else:
                files_with_issues += 1
                # Move files to mismatch folders
                shutil.move(os.path.join(coptic_folder, cop_file), mismatch_coptic_folder)
                shutil.move(os.path.join(arabic_folder, arb_file), mismatch_arabic_folder)
        else:
            files_with_issues += 1  # Count as issue if no match found

# Print the summary of processing
print(f"Total Coptic files processed: {total_files}")
print(f"Number of parallel files processed: {parallel_files}")
print(f"Number of files with issues (mismatch or no match): {files_with_issues}")

