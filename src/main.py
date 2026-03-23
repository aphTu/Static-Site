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

md = """
> Normal Quote
> **Bold** Quote
> _Italic_ Quote
>![image](quote)
>[link](quote)


"""

md2 = """
- hey
- hey 2
- hey 3 **bruh**

1. hello 
2. _hello_ italicize
3. this is **bold** and _italicize_ hello
"""
print(markdown_to_html_node(md))
# markdown_to_html_node(md2)

if __name__ == "__main__":
    main()
