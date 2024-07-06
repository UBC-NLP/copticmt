from os import path, listdir
from pathlib import Path
import pandas as pd
from tqdm import tqdm
import argparse
from models.coptic import CopticBible
from utils import write_verses, list_directory_contents


coptic_numbers = [
    # 1    2    3   4   5   6    7    8    9   10
    "ⲁ̅", "ⲃ̅", "ⲅ̅", "ⲇ̅", "ⲉ̅", "Ⲋ", "ⲍ̅", "ⲏ̅", "ⲑ̅", "ⲓ̅",
    # 11  12    13   14   15   16   17    18   19   20
    "ⲓ̅ⲁ̅", "ⲓ̅ⲃ̅", "ⲓ̅ⲅ̅", "ⲓ̅ⲇ̅", "ⲓ̅ⲉ̅", "ⲓ̅Ⲋ", "ⲓ̅ⲍ̅", "ⲓ̅ⲏ̅", "ⲓ̅ⲑ̅", "ⲕ̅",
    # 21   22    23   24    25    26    27   28    29   30
    "ⲕ̅ⲁ̅", "ⲕ̅ⲃ̅", "ⲕ̅ⲅ̅", "ⲕ̅ⲇ̅", "ⲕ̅ⲉ̅", "ⲕ̅Ⲋ", "ⲕ̅ⲍ̅", "ⲕ̅ⲏ̅", "ⲕ̅ⲑ̅", "ⲗ̅",
    # 40  50   60   70   80   90  100  200
    "ⲙ̅", "ⲛ̅", "ⲝ̅", "ⲟ̅", "ⲡ̅"]


def process_bible_texts(chapter_path: str, category: str):
    df = pd.DataFrame()
    coptic_bible = CopticBible(chapter_path, category)

    for verse in coptic_bible.verses:
        new_row = pd.DataFrame({
            "Book Category": [coptic_bible.category],
            "Book Name": [coptic_bible.book_name],
            "Chapter": [coptic_bible.chapter],
            "Verse": [verse.verse],
            "Translation": [verse.translation],
            "Number": [verse.number]})

        df = pd.concat([df, new_row]).reset_index(drop=True)
    return df


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Process a coptic bible with html format.")
    parser.add_argument("category_dir",
                        help="Path to the html file to process.")
    parser.add_argument("output_dir",
                        help="Path to the dataset file to write.")

    category_dir = parser.parse_args().category_dir
    output_dir = parser.parse_args().output_dir

    df = pd.DataFrame()
    category_texts = list_directory_contents(category_dir)
    category = path.basename(path.normpath(category_dir))
    print(f"Processing {category}'s texts.")
    for filename in tqdm(category_texts):
        old_df = process_bible_texts(
            path.join(category_dir, filename), category)
        if old_df is not None:
            df = pd.concat([df, old_df])

    write_verses(df, output_dir, category)
