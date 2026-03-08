from utilities.textnode import *
from utilities.htmlnode import HTMLNode, LeafNode
from utilities.delimiter import split_nodes_delimiter, parse_inline
from utilities.markdown_link import split_nodes_links
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

    text = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT)
    print(split_nodes_links([text]))

if __name__ == "__main__":
    main()
