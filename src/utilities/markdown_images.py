import re
from utilities.textnode import TextType,TextNode
def extract_markdown_images(text):
  ## takes raw markdown images 
  ## return a list of tuples, with an alt text and url for the markdown image

  markdown_images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

  return markdown_images
def split_nodes_images(old_nodes):
  nodes = []
  for node in old_nodes:
    # print(f"node: {node}")
    if node.text_type != TextType.TEXT:
      nodes.append(node)
      continue
    text = node.text
    extracted_links = extract_markdown_images(text)
    if len(extracted_links) == 0:
      nodes.append(node)
      continue
    splitted_text= text
    # print(f"outer: {splitted_text}")
    for anchor_text, image in extracted_links:
      splitted_text = splitted_text.split(f"![{anchor_text}]({image})",1)
      # print(f"len({len(splitted_text)})")
      # print(f"inside function: {splitted_text}")
      if(len(splitted_text)!=2):
        raise ValueError("invalid markdown, image section is not closed")
      if(splitted_text[0] != ""):
        nodes.append(TextNode(splitted_text[0], TextType.TEXT))
      # print(f"bruh1 {anchor_text}")
      nodes.append(TextNode(anchor_text,TextType.IMAGES, url=image))
      # print("bruh2")
      # print("\n")
      splitted_text = "".join(splitted_text[1:len(splitted_text) + 1])
    if(splitted_text != ""):
      nodes.append(TextNode(splitted_text, TextType.TEXT))
    # print(f"nodes currently: {nodes}")
    # print("\nNext One\n")

  # print(f"final nodes: {nodes}")
  return nodes
  