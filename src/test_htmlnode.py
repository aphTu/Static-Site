from htmlnode import HTMLNode, LeafNode, ParentNode
import unittest
class TestHTMLNode(unittest.TestCase):
  def test_props_to_html_Equal(self):
    node = HTMLNode("p", "hey buddy", None, {
    "href": "https://www.google.com",
    "target": "_blank",})
    self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")
  def test_props_to_html_notEqual(self):
    node = HTMLNode("p", "hey buddy", None, {
    "href": "https://www.google.com",
    "target": "_blank",})
    self.assertNotEqual(node.props_to_html(), "href=\"https://www.google.com\" target=\"_blank\"")
  def test_eq(self):
    node = HTMLNode("p", "hey buddy", None, None)
    self.assertEqual(node.tag, "p")
  
  def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    node.props = {"href": "https://www.google.com"}
    node.tag = "a"
    node.value = "Click me!"
    self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    node2 = LeafNode(None,value = "hey buddy", props = {"key": "bruh"})
    self.assertEqual(node2.to_html(), 'hey buddy')

  def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

  def test_to_html_with_grandchildren(self):
      grandchild_node = LeafNode("b", "grandchild")
      child_node = ParentNode("span", [grandchild_node])
      parent_node = ParentNode("div", [child_node])
      self.assertEqual(
          parent_node.to_html(),
          "<div><span><b>grandchild</b></span></div>",
      )
  def test_html_with_multiple_children_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    grandchild_node2 = LeafNode("i", "grandchild2")
    grandchild_node3 = LeafNode("p", "grandchild3")
    child_node = ParentNode("span", [grandchild_node])
    child_node2 = ParentNode("span", [grandchild_node2, grandchild_node3])
    parent_node = ParentNode("div", [child_node, child_node2])
    self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span><span><i>grandchild2</i><p>grandchild3</p></span></div>")

  def test_html_with_no_children(self):
    parent_node = ParentNode("div", None)
    self.assertRaises(ValueError,parent_node.to_html)

    

  