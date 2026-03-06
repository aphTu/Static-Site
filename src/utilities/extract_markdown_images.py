import re

def extract_markdown_images(text):
  ## takes raw markdown images 
  ## return a list of tuples, with an alt text and url for the markdown image
  alt_text = re.findall(r"!\[(.*?)\]",text)
  image_url = re.findall(r"\((.*?)\)", text)
  # if(len(alt_text) > len(image_url)):
  #   raise Exception("Missing url links for image, please include the url for the image")
  
  # if(len(alt_text) < len(image_url)):
  #   raise Exception("Missing alternative text for image, please include the alternative text")

  markdown_images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
  # for i in range(0, len(alt_text)):
  #   markdown_images.append((alt_text[i], image_url[i]))
  return markdown_images