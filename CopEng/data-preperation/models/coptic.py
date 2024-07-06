from enum import Enum
from typing import List
from models import Chapter, Verse
from utils import parse_document, extract_document_info, generate_verses, generate_chapters


class CopticSaintsLife:
    book_name: str
    category: str
    chapters: List[Chapter]

    def __init__(self, document_path: str, category: str):
        document = parse_document(document_path)
        self.category = category
        document_info = extract_document_info(document)
        self.book_name = document_info["title"]
        self.chapters = generate_chapters(document)


class CopticBible:
    category: str
    verses: List[Verse]
    book_name: str
    chapter: str

    def __init__(self, chapter_path: str, category: str):
        chapter_doc = parse_document(chapter_path)
        self.category = category
        document_info = extract_document_info(chapter_doc)
        self.book_name = document_info["title"]
        self.chapter = document_info["chapter"]
        self.verses = generate_verses(chapter_doc)
