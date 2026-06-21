from src.utils import clean_text


def test_clean_text_removes_extra_spaces_and_lowercases():
    text = "  This   Product is GOOD   "
    assert clean_text(text) == "this product is good"


def test_clean_text_handles_none():
    assert clean_text(None) == ""
