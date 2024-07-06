import subprocess

# List of your file groups
file_groups = [
    ['PATH TO/copticmt/CopEng/dataset/train/train.en', 'PATH TO/copticmt/CopEng/dataset/test/test.en', 'PATH TO/copticmt/CopEng/dataset/val/val.en'],
    ['PATH TO/copticmt/CopEng/dataset/train/train.coptic', 'PATH TO/copticmt/CopEng/dataset/test/test.coptic', 'PATH TO/copticmt/CopEng/dataset/val/val.coptic'],
    ['PATH TO/copticmt/CoPARA/dataset/train/train.coptic', 'PATH TO/copticmt/CoPARA/dataset/test/test.coptic', 'PATH TO/copticmt/CoPARA/dataset/val/val.coptic'],
    ['PATH TO/copticmt/CoPARA/dataset/train/train.ar', 'PATH TO/copticmt/CoPARA/dataset/test/test.ar', 'PATH TO/copticmt/CoPARA/dataset/val/val.ar']
]

# Path to the SentencePiece model
spm_model = 'PATH TO/copticmt/scripts/FairSeqTraining/M2M100/tokenizationFiles/spm.128k.model'

# Loop through each group of files
for group in file_groups:
    for file_name in group:
        # Set input and output file paths
        input_file = file_name
        output_file = file_name.split('.')[0] + '.m2m100.' + file_name.split('.')[1]

        # Build the command to execute
        command = [
            'python', 'PATH TO/fairseq/scripts/spm_encode.py',
            '--model', spm_model,
            '--output_format', 'piece',
            '--inputs', input_file,
            '--outputs', output_file
        ]

        # Execute the command
        subprocess.run(command)

        print(f"Processed {input_file} to {output_file}")

# Note: Ensure this script is run in an environment where Python and fairseq are installed and configured.
