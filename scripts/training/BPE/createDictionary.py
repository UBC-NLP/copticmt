import sentencepiece as spm
import os

# File paths for the training data
arabic_file = "PATH TO/copticmt/CoPARA/combined_arabic.txt"
# coptic_file = "PATH TO/copticmt/CopEng/dataset/processed/combined_coptic.txt"
# english_file = "PATH TO/copticmt/CopEng/dataset/processed/combined_english.txt"

# Model output directories
# english_spm_prefix = "PATH TO/copticmt/scripts/training/BPE/spmTrainer/English/english"
coptic_spm_prefix = "PATH TO/copticmt/scripts/training/BPE/spmTrainer/Coptic/coptic"
arabic_spm_prefix = "PATH TO/copticmt/scripts/training/BPE/spmTrainer/Arabic/arabic"

# # Train the SentencePiece models
# spm.SentencePieceTrainer.Train(f'--input={english_file} --model_prefix={english_spm_prefix} --vocab_size=12000 --model_type=bpe')
# spm.SentencePieceTrainer.Train(f'--input={coptic_file} --model_prefix={coptic_spm_prefix} --vocab_size=12000 --model_type=bpe')
spm.SentencePieceTrainer.Train(f'--input={arabic_file} --model_prefix={arabic_spm_prefix} --vocab_size=800 --model_type=bpe')

# # Function to tokenize files using a trained SentencePiece model
def tokenize_file(input_file, model_prefix, output_file):
    sp = spm.SentencePieceProcessor(model_file=model_prefix + '.model')
    with open(input_file, 'r', encoding='utf-8') as f, open(output_file, 'w', encoding='utf-8') as fo:
        for line in f:
            tokens = sp.encode(line, out_type=str)
            fo.write(" ".join(tokens) + "\n")

# Paths to files that need tokenization
english_files = [
    'PATH TO/copticmt/CopEng/dataset/train/train.en', 
    'PATH TO/copticmt/CopEng/dataset/test/test.en', 
    'PATH TO/copticmt/CopEng/dataset/val/val.en'
]

coptic_files = [
    'PATH TO/copticmt/CopEng/dataset/train/train.coptic', 
    'PATH TO/copticmt/CopEng/dataset/test/test.coptic', 
    'PATH TO/copticmt/CopEng/dataset/val/val.coptic'
]

coptic_arabic_files = [
    'PATH TO/copticmt/CoPARA/dataset/train/train.coptic', 
    'PATH TO/copticmt/CoPARA/dataset/test/test.coptic', 
    'PATH TO/copticmt/CoPARA/dataset/val/val.coptic'
]
arabic_files = [
    'PATH TO/copticmt/CoPARA/dataset/train/train.ar', 
    'PATH TO/copticmt/CoPARA/dataset/test/test.ar', 
    'PATH TO/copticmt/CoPARA/dataset/val/val.ar'
]

# Tokenize English files
# for file_name in english_files:
#     output_file = file_name.replace('.en', '.bpe.en')
#     tokenize_file(file_name, english_spm_prefix, output_file)

# # Tokenize Coptic files
# for file_name in coptic_files:
#     output_file = file_name.replace('.coptic', '.bpe.coptic')
#     tokenize_file(file_name, coptic_spm_prefix, output_file)

for file_name in coptic_arabic_files:
    output_file = file_name.replace('.coptic', '.bpe.coptic')
    tokenize_file(file_name, coptic_spm_prefix, output_file)

# Tokenize Arabic files
for file_name in arabic_files:
    output_file = file_name.replace('.ar', '.bpe.ar')
    tokenize_file(file_name, arabic_spm_prefix, output_file)
