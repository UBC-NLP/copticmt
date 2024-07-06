import os
import random
import argparse

def shuffle_and_split_files(file1_path, file2_path, train_percent, train_dir, val_dir, test_dir, val_percent=None):
    # Set random seed for reproducibility
    random.seed(42)

    # Calculate the percentage for val and test if not specified
    if val_percent is None:
        remaining = 100 - train_percent
        val_percent = remaining / 2
    test_percent = 100 - train_percent - val_percent

    # Ensure output directories exist
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # Read the contents of both files
    with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()

    # Ensure both files have the same number of lines
    assert len(lines1) == len(lines2), "Files are not parallel (different number of lines)"

    # Pair the lines to shuffle them together
    paired_lines = list(zip(lines1, lines2))
    random.shuffle(paired_lines)
    lines1, lines2 = zip(*paired_lines)

    # Calculate split indices
    total_lines = len(lines1)
    train_end = int(total_lines * (train_percent / 100))
    val_end = train_end + int(total_lines * (val_percent / 100))

    # Split the data
    train_data1, val_data1, test_data1 = lines1[:train_end], lines1[train_end:val_end], lines1[val_end:]
    train_data2, val_data2, test_data2 = lines2[:train_end], lines2[train_end:val_end], lines2[val_end:]

    # Save the split data to different folders
    save_split_data(train_data1, train_data2, os.path.basename(file1_path), os.path.basename(file2_path), train_dir, 'train')
    save_split_data(val_data1, val_data2, os.path.basename(file1_path), os.path.basename(file2_path), val_dir, 'val')
    save_split_data(test_data1, test_data2, os.path.basename(file1_path), os.path.basename(file2_path), test_dir, 'test')

    print("Files have been shuffled and split into separate folders for train, val, and test sets.")

def save_split_data(data1, data2, file1_name, file2_name, directory, split_name):
    file1_name = file1_name.replace('.txt', f'_{split_name}.txt')
    file2_name = file2_name.replace('.txt', f'_{split_name}.txt')
    with open(os.path.join(directory, file1_name), 'w', encoding='utf-8') as f1, \
         open(os.path.join(directory, file2_name), 'w', encoding='utf-8') as f2:
        f1.writelines(data1)
        f2.writelines(data2)

def main():
    parser = argparse.ArgumentParser(description='Shuffle and Split Text Files for Language Model Training')
    parser.add_argument('file1_path', type=str, help='Path to the first text file (e.g., file containing Coptic text)')
    parser.add_argument('file2_path', type=str, help='Path to the second text file (e.g., file containing English text)')
    parser.add_argument('train_percent', type=int, help='Percentage of data to use for training set')
    parser.add_argument('train_dir', type=str, help='Directory to store training files')
    parser.add_argument('val_dir', type=str, help='Directory to store valelopment files')
    parser.add_argument('test_dir', type=str, help='Directory to store test files')
    parser.add_argument('--val_percent', type=int, default=None, help='Optional: Specific percentage of data to use for valelopment set. If not set, remainder is split between val and test.')

    args = parser.parse_args()

    shuffle_and_split_files(
        args.file1_path,
        args.file2_path,
        args.train_percent,
        args.train_dir,
        args.val_dir,
        args.test_dir,
        args.val_percent
    )

if __name__ == "__main__":
    main()