from enum import Enum
from htmlnode import* 

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    LINK = "link"
    IMAGES = "images"
    CODE = "code"

class TextNode():
    def __init__(self,text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, other):
        if (self.text == other.text and self.text_type == other.text_type and self.url == other.url):
            return True
        return False
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
