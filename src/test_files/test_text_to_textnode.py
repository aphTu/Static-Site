from utilities.text_to_textnode import text_to_textnode
import unittest
from utilities.textnode import TextNode, TextType

class TestTextToTextNode(unittest.TestCase):
  def test_splitting_only_bold(self):
    text = "This is **text**"
    expected = [
      TextNode("This is ", TextType.TEXT),
      TextNode("text", TextType.BOLD)
    ]
    self.assertEqual(expected, text_to_textnode(text))

  def test_splitting_only_italic(self):
    text = "This is _text_"
    expected = [
      TextNode("This is ", TextType.TEXT),
      TextNode("text", TextType.ITALIC)
    ]
    self.assertEqual(expected, text_to_textnode(text))
  
  def test_splitting_only_code(self):
    print("hello")
    text = "This is `text`"
    expected = [
      TextNode("This is ", TextType.TEXT),
      TextNode("text", TextType.CODE)
    ]
    self.assertEqual(expected, text_to_textnode(text))

  def test_splitting_all_delimiter(self):
    text = "This is **text** with an _italic_ word and a `code block`"
    expected = [
      TextNode("This is ", TextType.TEXT),
      TextNode("text", TextType.BOLD),
      TextNode(" with an ", TextType.TEXT),
      TextNode("italic", TextType.ITALIC),
      TextNode(" word and a ", TextType.TEXT),
      TextNode("code block", TextType.CODE)
    ]
    self.assertEqual(expected, text_to_textnode(text))

  def test_splitting_only_image(self):
    text = "This is ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"
    expected =[
      TextNode("This is ", TextType.TEXT),
      TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg")
    ]
    self.assertEqual(expected, text_to_textnode(text))

  def test_splitting_only_link(self):
    text = "This is [link](https://boot.dev)"
    expected = [
      TextNode("This is ", TextType.TEXT),
      TextNode("link", TextType.LINK, "https://boot.dev")
    ]

    self.assertEqual(expected, text_to_textnode(text))

  def test_splitting_all_delimiter_and_image(self):
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"
    expected = [
      TextNode("This is ", TextType.TEXT),
      TextNode("text", TextType.BOLD),
      TextNode(" with an ", TextType.TEXT),
      TextNode("italic", TextType.ITALIC),
      TextNode(" word and a ", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode(" and an ", TextType.TEXT),
      TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg")
    ]
    self.assertEqual(expected, text_to_textnode(text))
  
  def test_splitting_everything(self):
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    expected = [
      TextNode("This is ", TextType.TEXT),
      TextNode("text", TextType.BOLD),
      TextNode(" with an ", TextType.TEXT),
      TextNode("italic", TextType.ITALIC),
      TextNode(" word and a ", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode(" and an ", TextType.TEXT),
      TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
      TextNode(" and a ", TextType.TEXT),
      TextNode("link", TextType.LINK, "https://boot.dev"),
    ]
    self.assertEqual(expected, text_to_textnode(text))
  
  def test_splitting_everything_back_to_back(self):
    text = "**text**_italic_`code block`[link](https://boot.dev)![image](https://link to image)"
    expected=[
      TextNode("text",TextType.BOLD),
      TextNode("italic", TextType.ITALIC),
      TextNode("code block", TextType.CODE),
      TextNode("link", TextType.LINK, "https://boot.dev"),
      TextNode("image", TextType.IMAGES, "https://link to image")
    ]
    self.assertEqual(expected, text_to_textnode(text))


  