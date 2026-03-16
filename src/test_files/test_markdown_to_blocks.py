from src.utilities.block_markdown import markdowns_to_blocks

import unittest

class TestMarkdownsToBlocks(unittest.TestCase):
  def test_markdown_to_blocks(self):
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    blocks = markdowns_to_blocks(md)
    expected =  [ 
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
          ]
    self.assertEqual(blocks, expected)

  def test_markdown_with_only_list(self):
    md = """
- This is a list
- With Items
- And More items
- With More Items
"""
    blocks = markdowns_to_blocks(md)
    expected = [
      "- This is a list\n- With Items\n- And More items\n- With More Items"
    ]
    self.assertEqual(blocks, expected)

  def test_markdown_with_only_paragraph(self):
    md = """
This is a paragraph
This is a new paragraph with a new line
3rd line
"""

    blocks = markdowns_to_blocks(md)
    expected = [
      "This is a paragraph\nThis is a new paragraph with a new line\n3rd line"
    ]
    self.assertEqual(blocks, expected)

  def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdowns_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

  def test_empty_string(self):
    md = ""
    blocks = markdowns_to_blocks(md)
    expected= []
    self.assertEqual(blocks,expected)

  def test_white_space_only(self):
    md = """        



"""
    blocks = markdowns_to_blocks(md)
    expected = [""]
    self.assertEqual(blocks,expected) 