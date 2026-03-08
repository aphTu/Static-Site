import unittest

from src.utilities.markdown_link import extract_markdown_links

class TestExtractMarkdownLinks(unittest.TestCase):
  def test_extract_one_link(self):
    text = "This is text with a link [to boot dev](https://www.boot.dev)"
    expected = [("to boot dev", "https://www.boot.dev")]
    self.assertEqual(expected, extract_markdown_links(text))
  
  def test_extracting_multiple_links(self):
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and go [to The Odin Project](https://www.theodinproject.com/dashboard) for front end development"
    expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev"), ("to The Odin Project", "https://www.theodinproject.com/dashboard")]

    self.assertEqual(expected, extract_markdown_links(text))

  def test_extracting_link_at_beginning(self):
    text = "[Boot dev](https://www.boot.dev) is a website to learn backend"
    expected = [("Boot dev", "https://www.boot.dev")]
    self.assertEqual(expected, extract_markdown_links(text))

  def test_extracting_link_at_end(self):
    text = "To learn backend go to [boot dev](https://www.boot.dev)"
    expected = [("boot dev", "https://www.boot.dev")]
    self.assertEqual(expected, extract_markdown_links(text))
  
  def test_extracting_link_at_front_and_end(self):
    text = "[Boot dev](https://www.boot.dev) is good, it as good as [The Odin Project](https://www.boot.dev)"
    expected = [("Boot dev", "https://www.boot.dev"), ("The Odin Project", "https://www.boot.dev")]
    self.assertEqual(expected, extract_markdown_links(text))

  def test_extracting_link_back_to_back(self):
    text="[back](https://www.boot.dev)[to back](https://www.boot.dev) test"
    expected = [("back", "https://www.boot.dev"), ("to back", "https://www.boot.dev")]
    self.assertEqual(expected, extract_markdown_links(text))
  
  def test_missing_parenthese(self):
    text = "[Boot dev](https://www.boot.dev and [The Odin Project](https://www.boot.dev) are good learning resources"
    expected = [('The Odin Project', "https://www.boot.dev")]

    self.assertEqual(expected, extract_markdown_links(text))

  def test_missing_brackets(self):
    text = "[Boot dev(https://www.boot.dev) and [The Odin Project(https://www.boot.dev)"
    expected = []

    self.assertEqual(expected, extract_markdown_links(text))
   
  
  def test_adding_an_image_instead_of_link(self):
    text = "![Boot dev](https://www.boot.dev)"
    expected = []
    self.assertEqual(expected, extract_markdown_links(text))
