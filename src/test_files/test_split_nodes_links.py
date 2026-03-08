from src.utilities.markdown_link import split_nodes_links
import unittest
from src.utilities.textnode import TextNode, TextType
class TestSplitMarkdownLinks(unittest.TestCase):
  # def test_splitting_node_with_one_link(self):
  #   node = TextNode("This is text with a link [to boot dev](https://www.boot.dev)", TextType.TEXT)
  #   expected = [
  #     TextNode("This is text with a link ",TextType.TEXT),
  #     TextNode("to boot dev", TextType.LINK, url="https://www.boot.dev")
  #               ]
  #   self.assertEqual(expected, split_nodes_links([node]))

  # def test_splitting_node_with_multiple_links(self):
  #   node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and go [to The Odin Project](https://www.theodinproject.com/dashboard) for front end development", TextType.TEXT)
  #   expected = [
  #     TextNode("This is text with a link ",TextType.TEXT),
  #     TextNode("to boot dev", TextType.LINK, url="https://www.boot.dev"),
  #     TextNode(" and ", TextType.TEXT),
  #     TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
  #     TextNode(" and go ", TextType.TEXT),
  #     TextNode("to The Odin Project", TextType.LINK, "https://www.theodinproject.com/dashboard"),
  #     TextNode(" for front end development", TextType.TEXT)
  #               ]
  #   self.assertEqual(expected, split_nodes_links([node]))

  def test_splitting_multiple_nodes_with_one_link(self):
    print("\n\nFailing One")
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