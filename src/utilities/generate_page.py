from src.utilities.block_markdown import markdown_to_html_node
from src.utilities.extract_title import extract_title
import os
from pathlib import Path

def generate_page(from_path, template_path,dest_path):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")
  from_file = open(from_path, "r")
  from_content = from_file.read()
  from_file.close()

  temp_file = open(template_path,"r")
  temp_content = temp_file.read()
  temp_file.close()
  from_html = markdown_to_html_node(from_content).to_html()
  title = extract_title(from_content)
  # print(f"\ntitle: {title}")
  # print(f"\nfrom_html: {from_html}")
  temp_content = temp_content.replace("{{ Title }}", title)
  temp_content =temp_content.replace("{{ Content }}", from_html)
  dest_dir = os.path.dirname(dest_path)
  if dest_dir != "":
    os.makedirs(dest_dir, exist_ok=True)
  # print(f"\ntemp_content: {temp_content}")
  dest_file = open(dest_path, "w")
  dest_file.write(temp_content)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
  # dir_path_content will takes in content
  # dest_dir_path will take in public directory
  list_of_directories= []
  if dir_path_content != "":
    list_of_directories = os.listdir(dir_path_content)
  else: 
    raise Exception("Please provide a valid directory for the dir_path_content")
  
  for directory in list_of_directories:
    content_path = os.path.join(dir_path_content, directory)
    dest_path = os.path.join(dest_dir_path,directory)
    if os.path.isfile(content_path):
      dest_path = Path(dest_path).with_suffix(".html")
      generate_page(content_path,template_path,dest_path)
    else:
      generate_pages_recursive(content_path,template_path,dest_path)