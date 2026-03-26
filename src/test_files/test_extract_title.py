import unittest
from src.utilities.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
  def test_simple_title(self):
    md = "# Hello"

    title = extract_title(md)
    expected = "Hello"
    self.assertEqual(title, expected)

  
