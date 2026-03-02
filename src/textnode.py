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
        raise Exception()
    
    Text_type = text_node.text_type
    match(Text_type):
        case TextType.TEXT:
            return LeafNode(None,text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {f"href": text_node.url})  
        case TextType.IMAGES:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"invalid text type: {text_node.text_type}")  

class InlineNode():
    def __init__(self, text_type, content = None, children = None):
        self.text_type = text_type
        self.content = content
        self.children = children if children is not None else []
    def __repr__(self):
        if self.children:
            return(f"InlineNode({self.text_type}, children= {self.children})")
        return (f"InlineNode({self.text_type}, {self.content!r})")
    def __eq__(self, other):
        # print(f"self: {self}")
        # print(f"other:{other}")
        return (self.text_type == other.text_type and self.content == other.content and self.children == other.children)
