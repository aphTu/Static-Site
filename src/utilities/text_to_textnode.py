from src.utilities.delimiter import split_nodes_images
from src.utilities.textnode import TextNode,TextType
from src.utilities.delimiter import split_nodes_delimiter, extract_markdown_links, split_nodes_links

def text_to_textnode(text):
  nodes = [TextNode(text,TextType.TEXT)]
  nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)
  # print(f"\n\nnodes after bold: {nodes}")
  nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
  # print(f"\n\nnodes after italic: {nodes}")
  nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
  nodes = split_nodes_images(nodes)
  # print(f"\n\nnodes after image: {nodes}")

  nodes = split_nodes_links(nodes)
  # print(f"\n\nnodes after link: {nodes}")

  return nodes