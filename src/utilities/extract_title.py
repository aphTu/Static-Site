
def extract_title(markdown):
  if markdown.startswith("# "):
    return " ".join(markdown.split("# "))
  else: 
    raise Exception("Missing title, please include the title using a singular #")
