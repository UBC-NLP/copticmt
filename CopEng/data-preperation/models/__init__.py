from typing import List


class Verse:
    # verse in coptic language
    verse: str
    number: str
    # translated verse in english
    translation: str

    def __init__(self, verse: str, number: str, translation: str) -> None:
        self.verse = verse
        self.number = number
        self.translation = translation


class Chapter:
    number: str
    verses: List[Verse]

    def __init__(self, number: str, verses: List[Verse]) -> None:
        self.number = number
        self.verses = verses
