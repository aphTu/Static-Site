# from src.utilities.textnode import TextNode,TextType
from src.utilities.htmlnode import HTMLNode, LeafNode
from src.utilities.block_markdown import markdown_to_html_node
from src.utilities.static_to_public import static_to_public
from src.utilities.generate_page import generate_pages_recursive
import sys

def main():
    print("hello world")
    # link = TextType.LINK
    # print(TextNode("this is some anchor text", link, "https://www.boot.dev" ))

    # node = LeafNode("p", "Hello, world!")
    # print(node.to_html())

    # delimiters = [
    #   ("**", TextType.BOLD),
    #   ("_", TextType.ITALIC),
    #   ("`", TextType.CODE),
    # ]

    # node = InlineNode(TextType.TEXT, content="This is an _italic and **bold** word_")
    # tree = parse_inline(node, delimiters)
    # print(tree)

# basepath= sys.argv[1] if sys.argv[1] else "/"
basepath = "/"
print(static_to_public(destination="docs", source="static"))

generate_pages_recursive("content", "template.html","docs", basepath)
# markdown_to_html_node(md2)
if __name__ == "__main__":
    main()
