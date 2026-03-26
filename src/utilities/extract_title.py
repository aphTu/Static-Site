
def extract_title(markdown):
  if markdown.startswith("# "):
    # print("\n\n\n\n")
    # print(markdown.split("# "))
    # print("".join(markdown.split("# ")))
    markdown ="".join(markdown.split("# "))
    markdown = markdown.split("\n")
    return markdown[0].strip()
    
  else: 
    raise Exception("Missing title, please include the title using a singular #")
