from src.utilities.delimiter import split_nodes_links
import unittest
from src.utilities.textnode import TextNode, TextType
class TestSplitMarkdownLinks(unittest.TestCase):
  def test_splitting_node_with_one_link(self):
    node = TextNode("This is text with a link [to boot dev](https://www.boot.dev)", TextType.TEXT)
    expected = [
      TextNode("This is text with a link ",TextType.TEXT),
      TextNode("to boot dev", TextType.LINK, url="https://www.boot.dev")
                ]
    self.assertEqual(expected, split_nodes_links([node]))

  def test_splitting_node_with_multiple_links(self):
    node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and go [to The Odin Project](https://www.theodinproject.com/dashboard) for front end development", TextType.TEXT)
    expected = [
      TextNode("This is text with a link ",TextType.TEXT),
      TextNode("to boot dev", TextType.LINK, url="https://www.boot.dev"),
      TextNode(" and ", TextType.TEXT),
      TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
      TextNode(" and go ", TextType.TEXT),
      TextNode("to The Odin Project", TextType.LINK, "https://www.theodinproject.com/dashboard"),
      TextNode(" for front end development", TextType.TEXT)
                ]
    self.assertEqual(expected, split_nodes_links([node]))

  def test_splitting_multiple_nodes_with_one_link(self):
    node = TextNode("This is text with a link [to boot dev](https://www.boot.dev)", TextType.TEXT)
    node2 = TextNode(" and [to youtube](https://www.youtube.com/@bootdotdev) and go", TextType.TEXT)
    node3 = TextNode("[to The Odin Project](https://www.theodinproject.com/dashboard) for front end development", TextType.TEXT)
    # print(split_nodes_links([node, node2, node3]))
    expected = [
      TextNode("This is text with a link ",TextType.TEXT),
      TextNode("to boot dev", TextType.LINK, url="https://www.boot.dev"),
      TextNode(" and ", TextType.TEXT),
      TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
      TextNode(" and go", TextType.TEXT),
      TextNode("to The Odin Project", TextType.LINK, "https://www.theodinproject.com/dashboard"),
      TextNode(" for front end development", TextType.TEXT)
                ]
    self.assertEqual(expected, split_nodes_links([node, node2, node3]))

  def test_splitting_multiple_nodes_with_multiples_links(self):
    node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [test](link) here", TextType.TEXT)
    node2 = TextNode(" and [to youtube](https://www.youtube.com/@bootdotdev) and [test2](link2) here", TextType.TEXT)
    node3 = TextNode("[to The Odin Project](https://www.theodinproject.com/dashboard) for front end development and [test3](link3) here", TextType.TEXT)
    # print(split_nodes_links([node, node2, node3]))
    expected = [
    TextNode("This is text with a link ",TextType.TEXT),
    TextNode("to boot dev", TextType.LINK, url="https://www.boot.dev"),
    TextNode(" and ", TextType.TEXT),
    TextNode("test", TextType.LINK, "link"),
    TextNode(" here", TextType.TEXT),
    TextNode(" and ", TextType.TEXT),
    TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"), 
    TextNode(" and ", TextType.TEXT),
    TextNode("test2", TextType.LINK, "link2"),
    TextNode(" here", TextType.TEXT),
    TextNode("to The Odin Project", TextType.LINK, "https://www.theodinproject.com/dashboard"),
    TextNode(" for front end development and ", TextType.TEXT),
    TextNode("test3", TextType.LINK, "link3"),
    TextNode(" here", TextType.TEXT),
              ]
    self.assertEqual(expected, split_nodes_links([node, node2, node3]))

  def test_splitting_node_with_link_at_beginning(self):
    node = TextNode("[Test](link2)This is text with a link [to boot dev](https://www.boot.dev) and [test](link) here", TextType.TEXT)
    expected =[
      TextNode("Test", TextType.LINK, "link2"),
      TextNode("This is text with a link ", TextType.TEXT),
      TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
      TextNode(" and ", TextType.TEXT),
      TextNode("test", TextType.LINK, "link"),
      TextNode(" here", TextType.TEXT)
    ]
    self.assertEqual(expected, split_nodes_links([node]))

  def test_splitting_nodes_with_link_at_beginning(self):
    node = TextNode("[begin](link_begin)This is text with a link [to boot dev](https://www.boot.dev) and [test](link) here", TextType.TEXT)
    node2 = TextNode("[begin2](link_begin2) and [to youtube](https://www.youtube.com/@bootdotdev) and [test2](link2) here", TextType.TEXT)
    node3 = TextNode("[to The Odin Project](https://www.theodinproject.com/dashboard) for front end development and [test3](link3) here", TextType.TEXT)
    # print(split_nodes_links([node, node2, node3]))
    expected = [
    TextNode("begin", TextType.LINK, "link_begin"),
    TextNode("This is text with a link ",TextType.TEXT),
    TextNode("to boot dev", TextType.LINK, url="https://www.boot.dev"),
    TextNode(" and ", TextType.TEXT),
    TextNode("test", TextType.LINK, "link"),
    TextNode(" here", TextType.TEXT),
    TextNode("begin2", TextType.LINK, "link_begin2"),
    TextNode(" and ", TextType.TEXT),
    TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"), 
    TextNode(" and ", TextType.TEXT),
    TextNode("test2", TextType.LINK, "link2"),
    TextNode(" here", TextType.TEXT),
    TextNode("to The Odin Project", TextType.LINK, "https://www.theodinproject.com/dashboard"),
    TextNode(" for front end development and ", TextType.TEXT),
    TextNode("test3", TextType.LINK, "link3"),
    TextNode(" here", TextType.TEXT),
              ]
    self.assertEqual(expected, split_nodes_links([node, node2, node3]))

  def test_splitting_node_with_link_at_end(self):
    node = TextNode("[Test](link2)This is text with a link [to boot dev](https://www.boot.dev) and [test](link)", TextType.TEXT)
    expected =[
      TextNode("Test", TextType.LINK, "link2"),
      TextNode("This is text with a link ", TextType.TEXT),
      TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
      TextNode(" and ", TextType.TEXT),
      TextNode("test", TextType.LINK, "link")
    ]
    self.assertEqual(expected, split_nodes_links([node]))

  def test_splitting_nodes_with_link_at_end(self):
    node = TextNode("[begin](link_begin)This is text with a link [to boot dev](https://www.boot.dev) and [test](link)", TextType.TEXT)
    node2 = TextNode("[begin2](link_begin2) and [to youtube](https://www.youtube.com/@bootdotdev) and [test2](link2)", TextType.TEXT)
    node3 = TextNode("[to The Odin Project](https://www.theodinproject.com/dashboard) for front end development and [test3](link3)", TextType.TEXT)
    # print(split_nodes_links([node, node2, node3]))
    expected = [
    TextNode("begin", TextType.LINK, "link_begin"),
    TextNode("This is text with a link ",TextType.TEXT),
    TextNode("to boot dev", TextType.LINK, url="https://www.boot.dev"),
    TextNode(" and ", TextType.TEXT),
    TextNode("test", TextType.LINK, "link"),
    TextNode("begin2", TextType.LINK, "link_begin2"),
    TextNode(" and ", TextType.TEXT),
    TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"), 
    TextNode(" and ", TextType.TEXT),
    TextNode("test2", TextType.LINK, "link2"),
    TextNode("to The Odin Project", TextType.LINK, "https://www.theodinproject.com/dashboard"),
    TextNode(" for front end development and ", TextType.TEXT),
    TextNode("test3", TextType.LINK, "link3"),
              ]
    self.assertEqual(expected, split_nodes_links([node, node2, node3]))

  def test_splitting_node_with_link_back_to_back(self):
    node = TextNode("[begin](link_begin)[test](link) testing", TextType.TEXT  )
    expected = [
      TextNode("begin", TextType.LINK, "link_begin"),
      TextNode("test", TextType.LINK, "link"),
      TextNode(" testing", TextType.TEXT)
    ]
    
    self.assertEqual(expected, split_nodes_links([node]))

  def test_non_text_node(self):
    node = TextNode("**Bolded Text**", TextType.BOLD)
    expected = [
      TextNode("**Bolded Text**", TextType.BOLD)
    ]
    self.assertEqual(expected, split_nodes_links([node]))
  
  def test_no_link(self):
    node = TextNode("this is a normal text", TextType.TEXT)
    expected = [
      TextNode("this is a normal text", TextType.TEXT)
    ]
    self.assertEqual(expected, split_nodes_links([node]))
  
  def test_node_with_image_instead_link(self):
    node = TextNode("This is ![alt_text](link)", TextType.TEXT)
    expected = [
      TextNode("This is ![alt_text](link)", TextType.TEXT)
    ]
    self.assertEqual(expected, split_nodes_links([node]))

