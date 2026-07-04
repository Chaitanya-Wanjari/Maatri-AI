import re


DEVANAGARI = re.compile(r"[\u0900-\u097F]")


def detect_language(text: str) -> str:
    """
    Detect Hindi vs English.

    Returns:
        hi
        en
    """

    if DEVANAGARI.search(text):
        return "hi"

    return "en"