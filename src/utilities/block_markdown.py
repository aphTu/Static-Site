from enum import Enum
from src.utilities.htmlnode import HTMLNode, ParentNode,LeafNode
from src.utilities.textnode import TextNode, TextType, text_node_to_html_node
from src.utilities.delimiter import split_nodes_delimiter
from src.utilities.delimiter import extract_markdown_images,split_nodes_images
from src.utilities.delimiter import extract_markdown_links, split_nodes_links
from src.utilities.text_to_textnode import text_to_textnode

class BlockType(Enum):
  PARAGRAPH = "paragraph"
  HEADING =  "heading"
  CODE = "code"
  QUOTE = "quote"
  UNORDERED_LIST = "unordered_list"
  ORDERED_LIST = "ordered_list"

def markdowns_to_blocks(markdown):
  # take in a markdown string
  # return list of "block" string
  markdown = markdown.split("\n\n")
  splitted_text = []
  for text in markdown:
    if(text != ""):
      splitted_text.append(text.strip())
  return splitted_text


def block_to_block_type(block):
  # take a single block of markdown text
  # return Blocktype representing what kinda block that is
  type_of_block = BlockType.PARAGRAPH
  lines = block.split("\n")
  if (block.startswith("# ") or block.startswith("## ") or block.startswith("### ") or block.startswith("#### ") or block.startswith("##### ") or block.startswith("###### ")):
    type_of_block = BlockType.HEADING
    return type_of_block

  if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
    type_of_block = BlockType.CODE
    return type_of_block
  
  if block.startswith(">"):
    for line in lines:
      if not line.startswith(">"):
        return type_of_block
    type_of_block = BlockType.QUOTE
    return type_of_block
  
  if block.startswith("- "):
    for line in lines:
      if not line.startswith("- "):
        return type_of_block
    type_of_block = BlockType.UNORDERED_LIST
    return type_of_block
  if block.startswith("1. "):
    for i in range(0,len(lines)):
      if not lines[i].startswith(f"{i+1}. "):
        return type_of_block
    type_of_block = BlockType.ORDERED_LIST
    return type_of_block
    
  # if("#" in block[0]):
  #   count = 0
  #   for i in range(1, 7):
  #     if(block[i] != "#"):
  #       break
  #     else:
  #       count+=1
  #   if(count > 6):
  #     raise Exception("Heading block can only have up to 6 #")
  #   if  block[count + 1] !=  " ":
  #     raise Exception("Please include a space between heading text and #")
  #   type_of_block = BlockType.HEADING

  # elif("```" in block[0:4]):
  #   if block.count("```") %2 != 0:
  #     raise Exception("Code block was not closed")
  #   block = block.split("\n")
  #   if block[0] == "```" and block[len(block)-1] == "```":
  #     type_of_block = BlockType.CODE
  
  # elif(">" in block[0]):
  #   block = block.split("\n")  
  #   for line in block:
  #     if line[0] == ">":
  #       type_of_block = BlockType.QUOTE
  #     else:
  #       type_of_block = BlockType.PARAGRAPH

  # elif ("-" in block[0]):
  #   block = block.split("\n")
  #   for line in block:
  #     if "- " in line[:2]:
  #       type_of_block = BlockType.UNORDERED_LIST
  #     else:
  #       type_of_block = BlockType.PARAGRAPH
  
  # elif ("." in block[1]):
  #   block = block.split("\n")
  #   for i in range(0, len(block)):
  #     if f"{i+1}. " in block[i][:3]:
  #       type_of_block = BlockType.ORDERED_LIST
  #     else:
  #       type_of_block = BlockType.PARAGRAPH
  return type_of_block

def markdown_to_html_node(markdown):
  #* convert an entire markdown to an parent html node, with nested elements
  html_nodes = []
  blocks = markdowns_to_blocks(markdown)
  # print(f"blocks:{blocks}")
  for block in blocks:
    type_of_block = block_to_block_type(block)
    match type_of_block:
      case BlockType.HEADING:
        html_nodes.append(heading_block_to_html_node(block))
      case BlockType.PARAGRAPH:
        html_nodes.append(paragraph_block_to_html_node(block))
      case BlockType.CODE:
        html_nodes.append(code_block_to_html_node(block))
  # div_parent  = ParentNode("div", html_nodes)
  # print(div_parent.to_html())
  

    

def heading_block_to_html_node(block):
  tag  = None
  heading_level = 0
  if(block.startswith("#")):
    tag = "h1"
  elif block.startswith("##"):
    tag = "h2"
    heading_level = 1
  elif block.startswith("###"):
    tag = "h3"
    heading_level = 2

  elif block.startswith("####"):
    tag = "h4"
    heading_level = 3

  elif block.startswith("#####"):
    tag = "h5"
    heading_level = 4

  else:
    tag = "h6"
    heading_level = 5

  if tag is None:
    raise Exception("Error with heading block")
  block = block.split(" ")
  del block[:heading_level+1]
  " ".join(block)
  print(block)  
  

def paragraph_block_to_html_node(block):
  tag = "p"
  block = block.split("\n")
  value = text_to_textnode(" ".join(block))
  # print(f"value: {value}")
  children=[]
  for node in value:
    # print(node)
    children.append(text_node_to_html_node(node))
  parent_node = ParentNode(tag, children=children)
  # print(f"ParentNode: {parent_node}")
  # print(f"ParentNode to html tag: {parent_node.to_html()}")
  return parent_node

def code_block_to_html_node(block):
  pass
  
