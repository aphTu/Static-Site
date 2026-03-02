from delimiter import *

import unittest 
class TestDelimiter(unittest.TestCase):
  def test_code_delimiter(self):
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),])

  def test_italic_delimiter(self):
    node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),
    TextNode("italic block", TextType.ITALIC),
    TextNode(" word", TextType.TEXT),])

  def test_bold_delimiter(self):
    node = TextNode("This is text with a **bolded phrase** in the middle",TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),
    TextNode("bolded phrase", TextType.BOLD),
    TextNode(" in the middle", TextType.TEXT),])

  def test_bold_delimiter_multiple(self):
    node = TextNode("This is text with a **bolded phrase** in the middle",TextType.TEXT)
    node2 = TextNode("this is a text 2 with ** bolded phrase** in the middle", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node,node2], "**", TextType.BOLD)
    self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),
    TextNode("bolded phrase", TextType.BOLD),
    TextNode(" in the middle", TextType.TEXT), 
    TextNode("this is a text 2 with ",TextType.TEXT),
    TextNode(" bolded phrase", TextType.BOLD),
    TextNode(" in the middle", TextType.TEXT) ])
  
  def test_italic_delimiter_two_delimiter_in_node(self):
    node = TextNode("This is text with a _italic phrase_ and _italic again_ in the middle",TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    self.assertEqual(new_nodes, 
    [TextNode("This is text with a ", TextType.TEXT),
    TextNode("italic phrase", TextType.ITALIC),
    TextNode(" and ", TextType.TEXT),
    TextNode("italic again", TextType.ITALIC),
    TextNode(" in the middle", TextType.TEXT),
    ])
  
  def test_unbalance_delimiter(self):
    node = TextNode("This is text with an _unblanced delimiter ",TextType.TEXT)
    with self.assertRaises(Exception):
      split_nodes_delimiter([node],"_", TextType.ITALIC)

  def test_delimiter_at_boundaries(self):
    node = TextNode("_This is text_ with a _italic phrase_ and _italic again_ in _the middle_",TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    self.assertEqual(new_nodes, 
    [
    TextNode("This is text", TextType.ITALIC),
    TextNode(" with a ", TextType.TEXT),
    TextNode("italic phrase", TextType.ITALIC),
    TextNode(" and ", TextType.TEXT),
    TextNode("italic again", TextType.ITALIC),
    TextNode(" in ", TextType.TEXT),
    TextNode("the middle", TextType.ITALIC)
    ])
  def test_non_text_node(self):
    node = TextNode("This is a text with a **bolded phrase** in the middle",TextType.BOLD)
    node2 = TextNode("this is a text 2 with ** bolded phrase** in the middle", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node,node2], "**", TextType.BOLD)
    self.assertEqual(new_nodes, 
    [
    TextNode("This is a text with a **bolded phrase** in the middle", TextType.BOLD),
    TextNode("this is a text 2 with ",TextType.TEXT),
    TextNode(" bolded phrase", TextType.BOLD),
    TextNode(" in the middle", TextType.TEXT) 
    ])
  def test_no_delimiter(self):
    node = TextNode("This is a text with a normal text", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(new_nodes, [TextNode("This is a text with a normal text", TextType.TEXT)])