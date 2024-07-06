import argparse
import os
import pandas as pd

def clean_concat_split_csv(files, output_coptic, output_english):
    dfs = [pd.read_csv(file) for file in files]
    concatenated_df = pd.concat(dfs, ignore_index=True)
    
    # Remove rows where Translation column contains "Not Found"
    concatenated_df = concatenated_df[concatenated_df["Translation"] != "Not Found"]
    
    concatenated_df.rename(columns={"Verse": "Coptic", "Translation": "English"}, inplace=True)
    
    # Remove rows with empty or "..." content in both Coptic and English columns
    concatenated_df = concatenated_df[(concatenated_df["Coptic"] != "...") & (concatenated_df["Coptic"] != "") & 
                                      (concatenated_df["English"] != "...") & (concatenated_df["English"] != "")]
    
    # Convert column values to strings and save Coptic and English columns in separate text files
    with open(output_coptic, 'w', encoding='utf-8') as coptic_file:
        coptic_file.write('\n'.join(map(str, concatenated_df["Coptic"])))
    
    with open(output_english, 'w', encoding='utf-8') as english_file:
        english_file.write('\n'.join(map(str, concatenated_df["English"])))
    
    print("Data concatenated, cleaned, and saved successfully.")

def main():
    parser = argparse.ArgumentParser(description="Clean, concatenate, and split CSV files in a directory.")
    parser.add_argument("--input_directory", default="dataset", help="Directory containing CSV files to concatenate")
    parser.add_argument("--output_coptic", default="dataset/processed/coptic.txt", help="Output Coptic text file")
    parser.add_argument("--output_english", default="dataset/processed/english.txt", help="Output English text file")

    args = parser.parse_args()
    
    input_files = [os.path.join(args.input_directory, file) for file in os.listdir(args.input_directory) if file.endswith(".csv")]
    if len(input_files) < 2:
        print("At least two CSV files are needed for concatenation.")
        return
    
    clean_concat_split_csv(input_files, args.output_coptic, args.output_english)

if __name__ == "__main__":
    main()
