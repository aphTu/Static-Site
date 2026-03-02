from htmlnode import *
from textnode import *
from collections import deque


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
    

def parse_inline(text, delimiter):
  ##! this entire thing is wrong, have to refix it, fucking ai giving me wrong implementation
  # Recursive function that check the sentence for every delimiter it has
  parsed = []
  if not delimiter:
    return [InlineNode(TextType.TEXT, content = text.content)]
  
  used_delimiter = delimiter[0]
  remaining_delimiter = delimiter[1:]
  splitted_text = text.content.split(used_delimiter[0])
  # print(splitted_text)
  if len(splitted_text)%2 == 0:
      raise Exception("Markdown error, delimiter was not closed")
  for i in range(0,len(splitted_text)):
    if splitted_text[i] == "":
      continue
    if i %2 != 0:
      # print(f"inside the i%2: {splitted_text}")
      node = InlineNode(used_delimiter[1], children=parse_inline(InlineNode(TextType.TEXT, splitted_text[i]), remaining_delimiter))
      parsed.extend([node])
    else:
      node = InlineNode(TextType.TEXT, content=splitted_text[i])
      parsed.extend(parse_inline(node, remaining_delimiter))
  return parsed
  
#* This function return earliest matching delimiters to split
def find_outer_delimiters(text, delimiters):
  ## delimiters is in this format:
      # ("**", TextType.BOLD),
      # ("_", TextType.ITALIC),
      # ("`", TextType.CODE),
  left_most = -1
  right_most = -2
    for delimiter in delimiters:
      
      
    
