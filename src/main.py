from textnode import *
from htmlnode import HTMLNode, LeafNode
from delimiter import split_nodes_delimiter, parse_inline
def main():
    print("hello world")
    # link = TextType.LINK
    # print(TextNode("this is some anchor text", link, "https://www.boot.dev" ))

    # node = LeafNode("p", "Hello, world!")
    # print(node.to_html())

    delimiters = [
      ("**", TextType.BOLD),
      ("_", TextType.ITALIC),
      ("`", TextType.CODE),
    ]

    text = "This is _italic and **bold** word_."
    tree = parse_inline(text, delimiters)
    print(tree)

if __name__ == "__main__":
    main()
