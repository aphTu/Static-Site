# from utilities.textnode import TextNode,TextType
from utilities.htmlnode import HTMLNode, LeafNode
from utilities.block_markdown import markdowns_to_blocks
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

    text = """
# This is a heading



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    print(markdowns_to_blocks(text))

if __name__ == "__main__":
    main()
