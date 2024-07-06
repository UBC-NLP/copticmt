import csv
import random
import os

def read_and_shuffle_to_tsv(file1_path, file2_path, output_tsv_path, prefix="Data"):
    # Set random seed for reproducibility
    random.seed(42)

    os.makedirs(os.path.dirname(output_tsv_path), exist_ok=True)

    # Read the contents of both files
    try:
        with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    if len(lines1) != len(lines2):
        print("Files are not parallel (different number of lines)")
        return

    # Pair the lines to shuffle them together
    paired_lines = list(zip(lines1, lines2))
    random.shuffle(paired_lines)
    shuffled_lines1, shuffled_lines2 = zip(*paired_lines)

    # Write the shuffled data to a TSV file
    try:
        with open(output_tsv_path, 'w', newline='', encoding='utf-8') as tsvfile:
            tsvwriter = csv.writer(tsvfile, delimiter='\t')  # Set delimiter to tab for TSV
            tsvwriter.writerow(['prefix', 'input_text', 'target_text'])  # Writing the headers
            for line1, line2 in zip(shuffled_lines1, shuffled_lines2):
                tsvwriter.writerow([prefix, line1.strip(), line2.strip()])  # Write each row
        print(f"TSV file created at: {output_tsv_path}")
    except Exception as e:
        print(f"Failed to write TSV file: {e}")

# Example usage
file1_path = 'PATH TO/copticmt/CoPARA/dataset/test/test.ar'
file2_path = 'PATH TO/copticmt/CoPARA/dataset/test/test.coptic'
output_tsv_path = 'PATH TO/copticmt/CoPARA/dataset/tsv/CopticArabicProcessedtest.tsv'

read_and_shuffle_to_tsv(file1_path, file2_path, output_tsv_path)
