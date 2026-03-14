from utilities.markdown_images import split_nodes_images
import unittest
from utilities.textnode import TextNode, TextType
class TestSplitMarkdownLinks(unittest.TestCase):
  def test_splitting_node_with_one_link(self):
    node = TextNode("This is text with an image ![to boot dev](https://www.boot.dev)", TextType.TEXT)
    expected = [
      TextNode("This is text with an image ",TextType.TEXT),
      TextNode("to boot dev", TextType.IMAGES, url="https://www.boot.dev")
                ]
    self.assertEqual(expected, split_nodes_images([node]))

  def test_splitting_node_with_multiple_links(self):
    node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev) and go ![to The Odin Project](https://www.theodinproject.com/dashboard) for front end development", TextType.TEXT)
    expected = [
      TextNode("This is text with a link ",TextType.TEXT),
      TextNode("to boot dev", TextType.IMAGES, url="https://www.boot.dev"),
      TextNode(" and ", TextType.TEXT),
      TextNode("to youtube", TextType.IMAGES, "https://www.youtube.com/@bootdotdev"),
      TextNode(" and go ", TextType.TEXT),
      TextNode("to The Odin Project", TextType.IMAGES, "https://www.theodinproject.com/dashboard"),
      TextNode(" for front end development", TextType.TEXT)
                ]
    self.assertEqual(expected, split_nodes_images([node]))

  def test_splitting_multiple_nodes_with_one_link(self):
    node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev)", TextType.TEXT)
    node2 = TextNode(" and ![to youtube](https://www.youtube.com/@bootdotdev) and go", TextType.TEXT)
    node3 = TextNode("![to The Odin Project](https://www.theodinproject.com/dashboard) for front end development", TextType.TEXT)
    # print(split_nodes_links([node, node2, node3]))
    expected = [
      TextNode("This is text with a link ",TextType.TEXT),
      TextNode("to boot dev", TextType.IMAGES, url="https://www.boot.dev"),
      TextNode(" and ", TextType.TEXT),
      TextNode("to youtube", TextType.IMAGES, "https://www.youtube.com/@bootdotdev"),
      TextNode(" and go", TextType.TEXT),
      TextNode("to The Odin Project", TextType.IMAGES, "https://www.theodinproject.com/dashboard"),
      TextNode(" for front end development", TextType.TEXT)
                ]
    self.assertEqual(expected, split_nodes_images([node, node2, node3]))

  def test_splitting_multiple_nodes_with_multiples_links(self):
    node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![test](image) here", TextType.TEXT)
    node2 = TextNode(" and ![to youtube](https://www.youtube.com/@bootdotdev) and ![test2](image2) here", TextType.TEXT)
    node3 = TextNode("![to The Odin Project](https://www.theodinproject.com/dashboard) for front end development and ![test3](image3) here", TextType.TEXT)
    # print(split_nodes_links([node, node2, node3]))
    expected = [
    TextNode("This is text with a link ",TextType.TEXT),
    TextNode("to boot dev", TextType.IMAGES, url="https://www.boot.dev"),
    TextNode(" and ", TextType.TEXT),
    TextNode("test", TextType.IMAGES, "image"),
    TextNode(" here", TextType.TEXT),
    TextNode(" and ", TextType.TEXT),
    TextNode("to youtube", TextType.IMAGES, "https://www.youtube.com/@bootdotdev"), 
    TextNode(" and ", TextType.TEXT),
    TextNode("test2", TextType.IMAGES, "image2"),
    TextNode(" here", TextType.TEXT),
    TextNode("to The Odin Project", TextType.IMAGES, "https://www.theodinproject.com/dashboard"),
    TextNode(" for front end development and ", TextType.TEXT),
    TextNode("test3", TextType.IMAGES, "image3"),
    TextNode(" here", TextType.TEXT),
              ]
    self.assertEqual(expected, split_nodes_images([node, node2, node3]))

  def test_splitting_node_with_link_at_beginning(self):
    node = TextNode("![Test](image2)This is text with a link ![to boot dev](https://www.boot.dev) and ![test](image) here", TextType.TEXT)
    expected =[
      TextNode("Test", TextType.IMAGES, "image2"),
      TextNode("This is text with a link ", TextType.TEXT),
      TextNode("to boot dev", TextType.IMAGES, "https://www.boot.dev"),
      TextNode(" and ", TextType.TEXT),
      TextNode("test", TextType.IMAGES, "image"),
      TextNode(" here", TextType.TEXT)
    ]
    self.assertEqual(expected, split_nodes_images([node]))

  def test_splitting_nodes_with_link_at_beginning(self):
    node = TextNode("![begin](image_begin)This is text with a link ![to boot dev](https://www.boot.dev) and ![test](image) here", TextType.TEXT)
    node2 = TextNode("![begin2](image_begin2) and ![to youtube](https://www.youtube.com/@bootdotdev) and ![test2](image2) here", TextType.TEXT)
    node3 = TextNode("![to The Odin Project](https://www.theodinproject.com/dashboard) for front end development and ![test3](image3) here", TextType.TEXT)
    # print(split_nodes_links([node, node2, node3]))
    expected = [
    TextNode("begin", TextType.IMAGES, "image_begin"),
    TextNode("This is text with a link ",TextType.TEXT),
    TextNode("to boot dev", TextType.IMAGES, url="https://www.boot.dev"),
    TextNode(" and ", TextType.TEXT),
    TextNode("test", TextType.IMAGES, "image"),
    TextNode(" here", TextType.TEXT),
    TextNode("begin2", TextType.IMAGES, "image_begin2"),
    TextNode(" and ", TextType.TEXT),
    TextNode("to youtube", TextType.IMAGES, "https://www.youtube.com/@bootdotdev"), 
    TextNode(" and ", TextType.TEXT),
    TextNode("test2", TextType.IMAGES, "image2"),
    TextNode(" here", TextType.TEXT),
    TextNode("to The Odin Project", TextType.IMAGES, "https://www.theodinproject.com/dashboard"),
    TextNode(" for front end development and ", TextType.TEXT),
    TextNode("test3", TextType.IMAGES, "image3"),
    TextNode(" here", TextType.TEXT),
              ]
    self.assertEqual(expected, split_nodes_images([node, node2, node3]))

  def test_splitting_node_with_link_at_end(self):
    node = TextNode("![Test](image2)This is text with a link ![to boot dev](https://www.boot.dev) and ![test](image)", TextType.TEXT)
    expected =[
      TextNode("Test", TextType.IMAGES, "image2"),
      TextNode("This is text with a link ", TextType.TEXT),
      TextNode("to boot dev", TextType.IMAGES, "https://www.boot.dev"),
      TextNode(" and ", TextType.TEXT),
      TextNode("test", TextType.IMAGES, "image")
    ]
    self.assertEqual(expected, split_nodes_images([node]))

  def test_splitting_nodes_with_link_at_end(self):
    node = TextNode("![begin](image_begin)This is text with a link ![to boot dev](https://www.boot.dev) and ![test](image)", TextType.TEXT)
    node2 = TextNode("![begin2](image_begin2) and ![to youtube](https://www.youtube.com/@bootdotdev) and ![test2](image2)", TextType.TEXT)
    node3 = TextNode("![to The Odin Project](https://www.theodinproject.com/dashboard) for front end development and ![test3](image3)", TextType.TEXT)
    # print(split_nodes_links([node, node2, node3]))
    expected = [
    TextNode("begin", TextType.IMAGES, "image_begin"),
    TextNode("This is text with a link ",TextType.TEXT),
    TextNode("to boot dev", TextType.IMAGES, url="https://www.boot.dev"),
    TextNode(" and ", TextType.TEXT),
    TextNode("test", TextType.IMAGES, "image"),
    TextNode("begin2", TextType.IMAGES, "image_begin2"),
    TextNode(" and ", TextType.TEXT),
    TextNode("to youtube", TextType.IMAGES, "https://www.youtube.com/@bootdotdev"), 
    TextNode(" and ", TextType.TEXT),
    TextNode("test2", TextType.IMAGES, "image2"),
    TextNode("to The Odin Project", TextType.IMAGES, "https://www.theodinproject.com/dashboard"),
    TextNode(" for front end development and ", TextType.TEXT),
    TextNode("test3", TextType.IMAGES, "image3"),
              ]
    self.assertEqual(expected, split_nodes_images([node, node2, node3]))

  def test_splitting_node_with_link_back_to_back(self):
    node = TextNode("![begin](image_begin)![test](image) testing", TextType.TEXT  )
    expected = [
      TextNode("begin", TextType.IMAGES, "image_begin"),
      TextNode("test", TextType.IMAGES, "image"),
      TextNode(" testing", TextType.TEXT)
    ]
    
    self.assertEqual(expected, split_nodes_images([node]))

  def test_non_text_node(self):
    node = TextNode("**Bolded Text**", TextType.BOLD)
    expected = [
      TextNode("**Bolded Text**", TextType.BOLD)
    ]
    self.assertEqual(expected, split_nodes_images([node]))
  
  def test_no_link(self):
    node = TextNode("this is a normal text", TextType.TEXT)
    expected = [
      TextNode("this is a normal text", TextType.TEXT)
    ]
    self.assertEqual(expected, split_nodes_images([node]))
  
  def test_node_with_link_instead_image(self):
    node = TextNode("This is [anchor_text](link)", TextType.TEXT)
    expected = [
      TextNode("This is [anchor_text](link)", TextType.TEXT)
    ]
    self.assertEqual(expected, split_nodes_images([node]))
