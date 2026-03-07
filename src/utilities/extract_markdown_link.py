import re

def extract_markdown_links(text):
  # take in a string that has markdown links
  # return list of tuples, with anchor text and URLS
  markdown_links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
  #have to include [^\[\]\] to prevent cases such as []( and []() from being counted as a correct markdown links
  return markdown_links