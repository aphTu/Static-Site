
def extract_title(markdown):
  if markdown.startswith("# "):
    print("\n\n\n\n")
    print(markdown.split("# "))
    print("".join(markdown.split("# ")))
    return " ".join(markdown.split("# ")).strip()
  else: 
    raise Exception("Missing title, please include the title using a singular #")
