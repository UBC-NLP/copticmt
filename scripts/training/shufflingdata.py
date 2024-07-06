import pandas as pd
import numpy as np

# Set a random seed for reproducibility
seed = 42
np.random.seed(seed)

# Read the CSV file
train = pd.read_csv("PATH TO/coptic-translator/dataset/processed/copticEnglish.csv")

# Shuffle the DataFrame
shuffled_train = train.sample(frac=1, random_state=seed)

# Save the shuffled DataFrame back to its original place
shuffled_train.to_csv("PATH TO/coptic-translator/dataset/processed/copticEnglish.csv", index=False)

# Print a message indicating completion
print("Data shuffled and saved with seed:", seed)
