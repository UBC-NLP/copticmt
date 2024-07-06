import html
from os import path, listdir
from pandas import DataFrame
from pathlib import Path
from typing import List
from bs4 import BeautifulSoup
from models import Verse, Chapter


def parse_document(document_path: str) -> BeautifulSoup:
    document = open(document_path, "r").read()
    # Some html files contains a numeric character reference (e.g. "&#11424;"
    # "&#1002;", "&#11440;"). To overcome this issue we have converted them to
    # the corresponding Unicode characters.
    return BeautifulSoup(
        html.unescape(document), features="lxml")


def extract_document_info(document: BeautifulSoup) -> str:
    return document.find("meta")


def generate_verses(document: BeautifulSoup) -> List[Verse]:
    chapter_verses: List[Verse] = []
    verses_tags = document.find_all("verse_n")
    for verse_tag in verses_tags:
        norms = verse_tag.find_all("norm_group")
        verse_text = " ".join([norm["norm_group"] for norm in norms])

        verse_translation = "Not Found"
        try:
            verse_translation = verse_tag["translation"]
        except KeyError:
            pass
        try:
            verse_translation = verse_tag.find("translation")[
                "translation"]
        except:
            pass

        chapter_verses.append(
            Verse(
                verse_text,
                verse_tag["verse_n"],
                verse_translation)
        )

    return chapter_verses


def generate_chapters(document: BeautifulSoup) -> List[Chapter]:
    chapters: List[Chapter] = []

    chapter_tags = document.find_all("chapter_n")
    for chapter_tag in chapter_tags:
        chapters.append(Chapter(
            chapter_tag["chapter_n"],
            generate_verses(chapter_tag)))
    return chapters


def write_verses(dataframe: DataFrame, output_dir: str, category: str):
    filepath = Path(path.join(output_dir, f"{category}.csv",))
    filepath.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(filepath, index=False)


def list_directory_contents(directory: str) -> List[str]:
    return [filename for filename in listdir(
        directory) if not filename.startswith(".")]
