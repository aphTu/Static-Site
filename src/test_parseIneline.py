from delimiter import *

import unittest
class TestParseInline(unittest.TestCase):
  # def test_just_italic(self):
  #   node = InlineNode(TextType.TEXT, content="This is _italic_ word")
  #   delimiter = [
  #     ("**", TextType.BOLD),
  #     ("_", TextType.ITALIC),
  #     ("`", TextType.CODE),
  #   ]
  #   new_nodes = parse_inline(node, delimiter)
  #   self.assertEqual(new_nodes,
  #   [
  #     InlineNode(TextType.TEXT, content= "This is "),
  #     InlineNode(TextType.ITALIC, children=[InlineNode(TextType.TEXT, content= "italic")]),
  #     InlineNode(TextType.TEXT, content= " word")
  #   ])
  
  # def test_just_code(self):
  #   node = InlineNode(TextType.TEXT, content="This is `code` word")
  #   delimiter = [
  #     ("**", TextType.BOLD),
  #     ("_", TextType.ITALIC),
  #     ("`", TextType.CODE),
  #   ]
  #   new_nodes = parse_inline(node, delimiter)
  #   self.assertEqual(new_nodes,
  #   [
  #     InlineNode(TextType.TEXT, content= "This is "),
  #     InlineNode(TextType.CODE, children=[InlineNode(TextType.TEXT, content= "code")]),
  #     InlineNode(TextType.TEXT, content= " word")
  #   ])
  
  # def test_just_bold(self):
  #   node = InlineNode(TextType.TEXT, content="This is **bold** word")
  #   delimiter = [
  #     ("**", TextType.BOLD),
  #     ("_", TextType.ITALIC),
  #     ("`", TextType.CODE),
  #   ]
  #   new_nodes = parse_inline(node, delimiter)
  #   self.assertEqual(new_nodes,
  #   [
  #     InlineNode(TextType.TEXT, content= "This is "),
  #     InlineNode(TextType.BOLD, children=[InlineNode(TextType.TEXT, content= "bold")]),
  #     InlineNode(TextType.TEXT, content= " word")
  #   ])

  # def test_bold_and_italic_not_nested(self):
  #   node = InlineNode(TextType.TEXT, content="This is _italic_ and **bold** word")
  #   delimiter = [
  #     ("**", TextType.BOLD),
  #     ("_", TextType.ITALIC),
  #     ("`", TextType.CODE),
  #   ]
  #   new_nodes = parse_inline(node, delimiter)
  #   self.assertEqual(new_nodes,
  #   [
  #     InlineNode(TextType.TEXT, content= "This is "),
  #     InlineNode(TextType.ITALIC, children=[InlineNode(TextType.TEXT, content= "italic")]),
  #     InlineNode(TextType.TEXT, content=" and "),
  #     InlineNode(TextType.BOLD, children=[InlineNode(TextType.TEXT, content="bold")]),
  #     InlineNode(TextType.TEXT, content= " word")
  #   ])


  # def test_italic_at_front(self):
  #   node = InlineNode(TextType.TEXT, content="_This_ is _italic_ and **bold** word")
  #   delimiter = [
  #     ("**", TextType.BOLD),
  #     ("_", TextType.ITALIC),
  #     ("`", TextType.CODE),
  #   ]
  #   new_nodes = parse_inline(node, delimiter)
  #   # print(new_nodes)
  
  #   self.assertEqual(new_nodes,
  #   [
  #     InlineNode(TextType.ITALIC, children=[InlineNode(TextType.TEXT, content= "This")]),
  #     InlineNode(TextType.TEXT, content= " is "),
  #     InlineNode(TextType.ITALIC, children=[InlineNode(TextType.TEXT, content= "italic")]),
  #     InlineNode(TextType.TEXT, content=" and "),
  #     InlineNode(TextType.BOLD, children=[InlineNode(TextType.TEXT, content="bold")]),
  #     InlineNode(TextType.TEXT, content= " word")
  #   ])

  # def test_italic_at_back(self):
  #   node = InlineNode(TextType.TEXT, content="_This_ is _italic_ and **bold** _word_")
  #   delimiter = [
  #     ("**", TextType.BOLD),
  #     ("_", TextType.ITALIC),
  #     ("`", TextType.CODE),
  #   ]
  #   new_nodes = parse_inline(node, delimiter)
  #   # print(new_nodes)

  #   self.assertEqual(new_nodes,
  #   [
  #     InlineNode(TextType.ITALIC, children=[InlineNode(TextType.TEXT, content= "This")]),
  #     InlineNode(TextType.TEXT, content= " is "),
  #     InlineNode(TextType.ITALIC, children=[InlineNode(TextType.TEXT, content= "italic")]),
  #     InlineNode(TextType.TEXT, content=" and "),
  #     InlineNode(TextType.BOLD, children=[InlineNode(TextType.TEXT, content="bold")]),
  #     InlineNode(TextType.TEXT, content=" "),
  #     InlineNode(TextType.ITALIC, children=[InlineNode(TextType.TEXT, content= "word")])
  #   ])
  
  def test_italic_nested_bold(self):
    # print("\n\n FALLING ONE")
    # node = InlineNode(TextType.TEXT, content="This is an _italic and **bold** word_")
    # delimiter = [
    #   ("**", TextType.BOLD),
    #   ("_", TextType.ITALIC),
    #   ("`", TextType.CODE),
    # ]
    # new_nodes = parse_inline(node, delimiter)
    # print(new_nodes)
    # self.assertEqual(new_nodes, [
    #   InlineNode(TextType.TEXT, content="This is an "),
    #   InlineNode(TextType.ITALIC, children=[
    #     InlineNode(TextType.TEXT, content= "italic and "),
    #     InlineNode(TextType.BOLD, children= [
    #       InlineNode(TextType.TEXT, content="bold")
    #     ]), 
    #     InlineNode(TextType.TEXT, content=" word")
    #   ])
    # ])
    delimiters = [
      ("**", TextType.BOLD),
      ("_", TextType.ITALIC),
      ("`", TextType.CODE),
    ]

    text = "This is _italic and **bold** word_."
    tree = parse_inline(text, delimiters)
    print(tree)

  