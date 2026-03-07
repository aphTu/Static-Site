import re

def extract_markdown_images(text):
  ## takes raw markdown images 
  ## return a list of tuples, with an alt text and url for the markdown image

  markdown_images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

  return markdown_images