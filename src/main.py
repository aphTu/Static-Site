from textnode import *
from htmlnode import HTMLNode, LeafNode
def main():
    print("hello world")
    link = TextType.LINK
    print(TextNode("this is some anchor text", link, "https://www.boot.dev" ))

    node = LeafNode("p", "Hello, world!")
    print(node.to_html())


if __name__ == "__main__":
    main()
