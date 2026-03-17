# from src.utilities.textnode import TextNode,TextType
from src.utilities.htmlnode import HTMLNode, LeafNode
from src.utilities.block_markdown import markdown_to_html_node
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

# md = """
# Heading hello sir

# This is **bolded** paragraph
# text in a p
# tag here

# This is another paragraph with _italic_ text and `code` here

# """
# markdown_to_html_node(md)

if __name__ == "__main__":
    main()
