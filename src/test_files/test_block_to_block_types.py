from utilities.block_markdown import block_to_block_type, BlockType, markdowns_to_blocks
import unittest

class TestBlockToBlockType(unittest.TestCase):
  def test_heading_block(self):
    md = """
###### This is a heading block with 6 #
"""
    block = "".join(markdowns_to_blocks(md))
    expected = BlockType.HEADING
    self.assertEqual(expected, block_to_block_type(block))

  def test_more_complicated_heading_block(self):
    md = """
##### #This is a heading block with 5 # and a space #
"""
    block = "".join(markdowns_to_blocks(md))
    expected = BlockType.HEADING
    self.assertEqual(expected, block_to_block_type(block))
  def test_heading_block_with_a_space_after_first_one(self):
    md = """
# ##### This is a heading block with 6 #
"""
    block = "".join(markdowns_to_blocks(md))
    expected = BlockType.HEADING
    self.assertEqual(expected, block_to_block_type(block))
  
  def test_heading_block_with_more_than_7(self):
    md = """
######## This is a heading block with 5 #
"""
    block = "".join(markdowns_to_blocks(md))
    expected = BlockType.PARAGRAPH
    self.assertEqual(expected, block_to_block_type(block))
  
  def test_heading_block_with_no_space_in_between(self):
    md = """
######This is a heading block with 5 #
"""
    block = "".join(markdowns_to_blocks(md))
    expected = BlockType.PARAGRAPH
    self.assertEqual(expected, block_to_block_type(block))

  def test_code_block(self):
    md = """
```
  print("hello world")
```
"""
    block = "".join(markdowns_to_blocks(md))
    expected = BlockType.CODE
    self.assertEqual(expected, block_to_block_type(block))

  def test_code_block_more_lines(self):
    md = """
```
  print("hello world")
  print("Welcome to Boot.Dev")
  print("this is a platform where you'll be learning backend development)
```
"""
    block = "".join(markdowns_to_blocks(md))
    expected = BlockType.CODE
    self.assertEqual(expected, block_to_block_type(block))

  def test_code_block_that_does_not_close(self):
    md = """
```
  print("hello world")
  print("Welcome to Boot.Dev")
  print("this is a platform where you'll be learning backend development)

"""
    block = "".join(markdowns_to_blocks(md))
    expected = BlockType.PARAGRAPH
    self.assertEqual(expected, block_to_block_type(block))

  def test_code_block_that_closed_prematurely(self):
    md = """
```
  print("hello world")
  print("Welcome to Boot.Dev")
  print("this is a platform where you'll be learning backend development)
```
  print("hello, this is outside of code block")
"""
    block = "".join(markdowns_to_blocks(md))
    expected = BlockType.PARAGRAPH
    self.assertEqual(expected, block_to_block_type(block))

  def test_quote_block(self):
    md = """
>print("hello world")
>print("Welcome to Boot.Dev")
>print("this is a platform where you'll be learning backend development)
"""
    block = "".join(markdowns_to_blocks(md))
    expected = BlockType.QUOTE
    self.assertEqual(expected, block_to_block_type(block))

  def test_missing_one_quote_delimiter(self):
    md = """
>print("hello world")
>print("Welcome to Boot.Dev")
this one does not have a quote at the beginning
"""
    block = "".join(markdowns_to_blocks(md))
    expected = BlockType.PARAGRAPH
    self.assertEqual(expected, block_to_block_type(block))

  def test_unordered_list(self):
    md = """
- print("hello world")
- print("Welcome to Boot.Dev")
- something
"""
    block = "".join(markdowns_to_blocks(md))
    expected = BlockType.UNORDERED_LIST
    self.assertEqual(expected, block_to_block_type(block))

  def test_unordered_list_with_no_space_between_word_and_delimiter(self):
    md = """
- print("hello world")
- print("Welcome to Boot.Dev")
-something
"""
    block = "".join(markdowns_to_blocks(md))
    expected = BlockType.PARAGRAPH
    self.assertEqual(expected, block_to_block_type(block))

  def test_unordered_list_missing_delimiter(self):
    md = """
- print("hello world")
- print("Welcome to Boot.Dev")
 something
"""
    block = "".join(markdowns_to_blocks(md))
    expected = BlockType.PARAGRAPH
    self.assertEqual(expected, block_to_block_type(block))

  def test_ordered_list(self):
    print("\n\nFAILLING ONE")
    md = """
1. print("hello world")
2. print("Welcome to Boot.Dev")
3. something
"""
    block = "".join(markdowns_to_blocks(md))
    expected = BlockType.ORDERED_LIST
    self.assertEqual(expected, block_to_block_type(block))

  def test_ordered_list_no_number_in_front(self):
    md = """
. print("hello world")
. print("Welcome to Boot.Dev")
. something
"""
    block = "".join(markdowns_to_blocks(md))
    expected = BlockType.PARAGRAPH
    self.assertEqual(expected, block_to_block_type(block))


