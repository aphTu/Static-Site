from src.utilities.markdown_images import split_nodes_images
from src.utilities.textnode import TextNode,TextType
from src.utilities.markdown_link import split_nodes_links
from src.utilities.delimiter import split_nodes_delimiter

def text_to_textnode(text):
  nodes = [TextNode(text,TextType.TEXT)]
  nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)
  nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
  nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
  nodes = split_nodes_images(nodes)
  nodes = split_nodes_links(nodes)
  return nodes