import re

def extract_markdown_links(text):
  # take in a string that has markdown links
  # return list of tuples, with anchor text and URLS
  markdown_links = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
  anchor_text = re.findall(r"(?<!!)\[(.*?)\]", text)
  url = re.findall(r"\((.*?)\)", text)
  # if len(anchor_text) > len(url):
  #   raise Exception("Missing url links for anchor text, please include the url for the link")
  
  # if len(anchor_text) < len(url):
  #   raise Exception("Missing anchor text for url, please include the anchor text for the link")
  
  # markdown_links = []
  # for i in range(0, len(anchor_text)):
  #   markdown_links.append((anchor_text[i],url[i]))
  return markdown_links