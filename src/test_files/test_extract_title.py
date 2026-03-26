import unittest
from src.utilities.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
  def test_simple_title(self):
    md = "# Hello"

    title = extract_title(md)
    expected = "Hello"
    self.assertEqual(title, expected)

  def test_longer_title(self):
    md = "# Hello this is a title"
    
    title = extract_title(md)
    expected = "Hello this is a title"
    self.assertEqual(title, expected)

  def test_with_trailing_whitespace(self):
    md = "# Hello this is a title                                    "
    
    title = extract_title(md)
    expected = "Hello this is a title"
    self.assertEqual(title, expected)

  def test_with_leading_whitespaces(self):
    md = "#                                 Hello this is a title"
    
    title = extract_title(md)
    expected = "Hello this is a title"
    self.assertEqual(title, expected)

  def test_with_leading_whitespaces_before_delimiter(self):
    md = "                   # Hello this is a title"
    with self.assertRaises(Exception):
      title = extract_title(md)

  def test_md_without_title(self):
    md = "Hello this is a title"
    
    with self.assertRaises(Exception):
      title = extract_title(md)
    