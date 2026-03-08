import re
from src.utilities.textnode import TextNode, TextType
def extract_markdown_links(text):
  # take in a string that has markdown links
  # return list of tuples, with anchor text and URLS
  markdown_links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
  #have to include [^\[\]\] to prevent cases such as []( and []() from being counted as a correct markdown links
  return markdown_links

def split_nodes_links(old_nodes):
  nodes = []
  for node in old_nodes:
    # print(f"node: {node}")
    if node.text_type != TextType.TEXT:
      nodes.append(node)
    text = node.text
    extracted_links = extract_markdown_links(text)
    splitted_text= text
    # print(f"outer: {splitted_text}")
    for anchor_text, link in extracted_links:
      splitted_text = splitted_text.split(f"[{anchor_text}]({link})",1)
      # print(f"len({len(splitted_text)})")
      # print(f"inside function: {splitted_text}")
      if(splitted_text[0] != ""):
        nodes.append(TextNode(splitted_text[0], TextType.TEXT))
      # print(f"bruh1 {anchor_text}")
      nodes.append(TextNode(anchor_text,TextType.LINK, url=link))
      # print("bruh2")
      # print("\n")
      splitted_text = "".join(splitted_text[1:len(splitted_text) + 1])
    if(splitted_text != ""):
      nodes.append(TextNode(splitted_text, TextType.TEXT))
    # print(f"nodes currently: {nodes}")
    # print("\nNext One\n")

  # print(f"final nodes: {nodes}")
  return nodes
