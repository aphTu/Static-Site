from src.utilities.block_markdown import markdown_to_html_node
from src.utilities.extract_title import extract_title
import os

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

