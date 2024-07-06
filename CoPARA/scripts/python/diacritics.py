import re

def remove_arabic_diacritics(text):
    arabic_diacritics = re.compile("""
                                 ّ    | # Shadda
                                 َ    | # Fatha
                                 ً    | # Tanwin Fath
                                 ُ    | # Damma
                                 ٌ    | # Tanwin Damm
                                 ِ    | # Kasra
                                 ٍ    | # Tanwin Kasr
                                 ْ    | # Sukun
                                 ـ     # Tatweel/Kashida
                             """, re.VERBOSE)
    return re.sub(arabic_diacritics, '', text)

# Define paths
input_file_path = "PATH TO/copticmt/CoPARA/processed_arabic.txt"
output_file_path = "PATH TO/copticmt/CoPARA/processed_arabicCleared.txt"

# Process the file
with open(input_file_path, 'r', encoding='utf-8') as file, \
     open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in file:
        cleaned_line = remove_arabic_diacritics(line)
        output_file.write(cleaned_line)

print("Diacritics have been removed and the output file is ready.")
