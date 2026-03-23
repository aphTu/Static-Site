from src.utilities.htmlnode import *
from src.utilities.textnode import TextNode, TextType, InlineNode
import copy
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
  # old_nodes is a list of previous nodes
  splitted = []
  # delimiter_start = False
  for node in old_nodes:
    delimiter_stack = []
    if node.text_type != TextType.TEXT:
      splitted.append(node)
      continue
    string_node_split = node.text.split(delimiter)
    if len(string_node_split) % 2 ==0:
      raise Exception("Markdown error, delimiter was not closed")
    # temp  =string_node_split.index(delimiter)
    # splitted.append(TextNode(string_node_split[0:temp], TextType.TEXT))
    # string_node_split = string_node_split[temp+1: ]
    # if delimiter not in string_node_split:
    #   raise Exception("Markdown error, delimiter was not closed")
    # else:
    #   temp = string_node_split.index(delimiter)
    # splitted.append(TextNode(string_node_split[:temp]), text_type)
    # string_node_split = string_node_split[temp+1:]
    # splitted.append(TextNode(string_node_split, TextType.TEXT))
    count = 0
    for _str in string_node_split:
      if (_str == ""):
        count+=1
        continue
      if (count %2 == 0 ):
        splitted.append(TextNode(_str, TextType.TEXT))
      elif (count%2==1):
        splitted.append(TextNode(_str,text_type))
      count+=1
  return splitted

def split_inline_delimiter(old_nodes, delimiter = None):
  splitted = []
  if delimiter is None:
    delimiter = [
      ("**", TextType.BOLD),
      ("_", TextType.ITALIC),
      ("`", TextType.CODE),
    ]
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
       splitted.append(node)
       continue
    

def parse_inline(text, delimiters):
  try:
    # Recursive function that check the sentence for every delimiters it has
    parsed = []
    if not delimiters:
      return [InlineNode(TextType.TEXT, content = text.content)]
    used_delimiter = find_outer_delimiters(text.content, delimiters)
    if used_delimiter is None:
      return [InlineNode(TextType.TEXT, content = text.content)]
      
    # print(f"used_delimiter:{used_delimiter}")
    remaining_delimiter = copy.deepcopy(delimiters)
    remaining_delimiter.remove(used_delimiter)
    # print(f"remaining_delimiter:{remaining_delimiter}")
    splitted_text = text.content.split(used_delimiter[0])
    # print(splitted_text)
    for i in range(0,len(splitted_text)):
      if splitted_text[i] == "":
        continue
      if i %2 != 0:
        # print(f"inside the i%2!=0: {splitted_text[i]}")
        node = InlineNode(used_delimiter[1], children=parse_inline(InlineNode(TextType.TEXT, splitted_text[i]), remaining_delimiter))
        parsed.extend([node])
      else:
        node = InlineNode(TextType.TEXT, content=splitted_text[i])
        parsed.extend(parse_inline(node, remaining_delimiter))
    return parsed
  except ValueError as e:
    raise Exception("Markdown error, delimiter was not closed")
  
#* This function return earliest matching delimiters to split, return None if there no matching delimiter to split
def find_outer_delimiters(text, delimiters):
 
  left_most = -1
  right_most = -1
  chosen_delimiter = None
  for delimiter in delimiters:
    # this get the first value of the set, which is the string for the delimiter
    current_delimiter = delimiter[0]
    if(current_delimiter not in text):
      continue
    temp_left = text.index(current_delimiter)
    # print(f"current_delimiter{current_delimiter}, temp_left: {temp_left}")
    # print(f"left_most: {left_most}")
    # print(f"text:{text}")

    if left_most == -1 or left_most > temp_left:
      left_most = temp_left
      right_most = text.index(current_delimiter, left_most + 1)
      # print(f"right_most:{right_most}")
      # print(f"left_most: {left_most}")
      chosen_delimiter = delimiter
  return chosen_delimiter
      
    
##* for markdown links
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
      continue
    text = node.text
    extracted_links = extract_markdown_links(text)
    if len(extracted_links) == 0:
      nodes.append(node)
      continue
    splitted_text= text
    # print(f"outer: {splitted_text}")
    for anchor_text, link in extracted_links:
      splitted_text = splitted_text.split(f"[{anchor_text}]({link})",1)
      # print(f"len({len(splitted_text)})")
      # print(f"inside function: {splitted_text}")
      # print("\n")
      if(len(splitted_text)!=2):
        raise ValueError("invalid markdown, image section is not closed")
      if(splitted_text[0] != ""):
        nodes.append(TextNode(splitted_text[0], TextType.TEXT))
      # print(f"bruh1 {anchor_text}")
      nodes.append(TextNode(anchor_text,TextType.LINK, url=link))
      # print("bruh2")
      # print("\n")
      splitted_text = (splitted_text[1])
    if(splitted_text != ""):
      nodes.append(TextNode(splitted_text, TextType.TEXT))
    # print(f"nodes currently: {nodes}")
    # print("\nNext One\n")

  # print(f"final nodes: {nodes}")
  return nodes

##* Markdown images
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

  return nodes
  