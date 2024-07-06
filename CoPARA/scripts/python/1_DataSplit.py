import os
import random

def shuffle_and_split_files(file1_path, file2_path, train_percent, train_dir, dev_dir, test_dir, dev_percent=None):
    # Set random seed for reproducibility
    random.seed(42)

    # Calculate the percentage for dev and test if not specified
    if dev_percent is None:
        remaining = 100 - train_percent
        dev_percent = remaining / 2
    test_percent = 100 - train_percent - dev_percent

    # Ensure output directories exist
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(dev_dir, exist_ok=True)
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
    dev_end = train_end + int(total_lines * (dev_percent / 100))

    # Split the data
    train_data1, dev_data1, test_data1 = lines1[:train_end], lines1[train_end:dev_end], lines1[dev_end:]
    train_data2, dev_data2, test_data2 = lines2[:train_end], lines2[train_end:dev_end], lines2[dev_end:]

    # Save the split data to different folders
    save_split_data(train_data1, train_data2, os.path.basename(file1_path), os.path.basename(file2_path), train_dir, 'train')
    save_split_data(dev_data1, dev_data2, os.path.basename(file1_path), os.path.basename(file2_path), dev_dir, 'dev')
    save_split_data(test_data1, test_data2, os.path.basename(file1_path), os.path.basename(file2_path), test_dir, 'test')

    print("Files have been shuffled and split into separate folders for train, dev, and test sets.")

def save_split_data(data1, data2, file1_name, file2_name, directory, split_name):
    file1_name = file1_name.replace('.txt', f'_{split_name}.txt')
    file2_name = file2_name.replace('.txt', f'_{split_name}.txt')
    with open(os.path.join(directory, file1_name), 'w', encoding='utf-8') as f1, \
         open(os.path.join(directory, file2_name), 'w', encoding='utf-8') as f2:
        f1.writelines(data1)
        f2.writelines(data2)

# Example usage:
shuffle_and_split_files(
    'PATH TO/copticmt/CoPARA/processed_arabicCleared.txt', 
    'PATH TO/copticmt/CoPARA/processed_coptic.txt', 
    80, 
    'PATH TO/copticmt/CoPARA/dataset/train', 
    'PATH TO/copticmt/CoPARA/dataset/test', 
    'PATH TO/copticmt/CoPARA/dataset/dev'
)
