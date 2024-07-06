import argparse
import os
from sklearn.model_selection import train_test_split

def split_and_save_text(input_coptic, input_english, output_dir):
    coptic_data = open(input_coptic, 'r', encoding='utf-8').readlines()
    english_data = open(input_english, 'r', encoding='utf-8').readlines()
    
    # Remove rows where Translation column contains "Not Found"
    data = [{"Coptic": coptic.strip(), "English": english.strip()} for coptic, english in zip(coptic_data, english_data) if english.strip() != "Not Found"]
    
    # Split the dataset into train, test, and dev sets
    train_data, temp_data = train_test_split(data, test_size=0.2, random_state=42)
    test_data, dev_data = train_test_split(temp_data, test_size=0.5, random_state=42)
    
    # Save datasets to separate text files
    with open(os.path.join(output_dir, "train.coptic"), 'w', encoding='utf-8') as train_coptic_file:
        train_coptic_file.write('\n'.join([item["Coptic"] for item in train_data]))
        
    with open(os.path.join(output_dir, "train.en"), 'w', encoding='utf-8') as train_english_file:
        train_english_file.write('\n'.join([item["English"] for item in train_data]))
        
    with open(os.path.join(output_dir, "test.coptic"), 'w', encoding='utf-8') as test_coptic_file:
        test_coptic_file.write('\n'.join([item["Coptic"] for item in test_data]))
        
    with open(os.path.join(output_dir, "test.en"), 'w', encoding='utf-8') as test_english_file:
        test_english_file.write('\n'.join([item["English"] for item in test_data]))
        
    with open(os.path.join(output_dir, "val.coptic"), 'w', encoding='utf-8') as dev_coptic_file:
        dev_coptic_file.write('\n'.join([item["Coptic"] for item in dev_data]))
        
    with open(os.path.join(output_dir, "val.en"), 'w', encoding='utf-8') as dev_english_file:
        dev_english_file.write('\n'.join([item["English"] for item in dev_data]))
    
    print("Data split and saved successfully.")

def main():
    parser = argparse.ArgumentParser(description="Split and save text dataset into train, test, and dev sets.")
    parser.add_argument("--input_coptic", default="dataset/processed/coptic.txt", help="Input Coptic text file")
    parser.add_argument("--input_english", default="dataset/processed/english.txt", help="Input English text file")
    parser.add_argument("--output_dir", default="dataset/split", help="Output directory for train, test, and dev text files")

    args = parser.parse_args()
    
    os.makedirs(args.output_dir, exist_ok=True)
    
    split_and_save_text(args.input_coptic, args.input_english, args.output_dir)

if __name__ == "__main__":
    main()
