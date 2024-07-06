import csv
import random
import os
import argparse

def read_and_shuffle_to_tsv(file1_path, file2_path, output_dir, prefix1, prefix2):
    # Set random seed for reproducibility
    random.seed(42)

    # Create output directory if it does not exist
    os.makedirs(output_dir, exist_ok=True)

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

    # Write the shuffled data to two TSV files
    output_paths = [os.path.join(output_dir, "File1_to_File2.tsv"), os.path.join(output_dir, "File2_to_File1.tsv")]
    prefixes = [prefix1, prefix2]
    file_pairs = [(shuffled_lines1, shuffled_lines2), (shuffled_lines2, shuffled_lines1)]
    
    for (output_path, prefix, (file1, file2)) in zip(output_paths, prefixes, file_pairs):
        try:
            with open(output_path, 'w', newline='', encoding='utf-8') as tsvfile:
                tsvwriter = csv.writer(tsvfile, delimiter='\t')
                tsvwriter.writerow(['prefix', 'input_text', 'target_text'])
                for line1, line2 in zip(file1, file2):
                    tsvwriter.writerow([prefix, line1.strip(), line2.strip()])
            print(f"TSV file created at: {output_path}")
        except Exception as e:
            print(f"Failed to write TSV file: {e}")

def main():
    parser = argparse.ArgumentParser(description="Create TSV files from parallel text files with specified prefixes.")
    parser.add_argument("file1_path", help="Path to the first text file (e.g., English text)")
    parser.add_argument("file2_path", help="Path to the second text file (e.g., Coptic text)")
    parser.add_argument("output_dir", help="Output directory for the TSV files")
    parser.add_argument("prefix1", help="Prefix for translating from file1 to file2")
    parser.add_argument("prefix2", help="Prefix for translating from file2 to file1")
    args = parser.parse_args()

    read_and_shuffle_to_tsv(args.file1_path, args.file2_path, args.output_dir, args.prefix1, args.prefix2)

if __name__ == "__main__":
    main()
