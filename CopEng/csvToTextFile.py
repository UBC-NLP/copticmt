import pandas as pd

# Load the CSV file
df = pd.read_csv("PATH TO/copticmt/old files/CopEng/copticEnglish.csv")

# Write the 'Coptic' column to a text file
with open("PATH TO/copticmt/CopEng/dataset/processed/coptic.txt", "w", encoding="utf-8") as file:
    file.write('\n'.join(df['Coptic'].astype(str)))

# Write the 'English' column to a text file
with open("PATH TO/copticmt/CopEng/dataset/processed/english.txt", "w", encoding="utf-8") as file:
    file.write('\n'.join(df['English'].astype(str)))

print("Files have been successfully written.")
