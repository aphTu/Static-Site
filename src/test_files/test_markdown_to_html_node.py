from src.utilities.block_markdown import markdown_to_html_node
import unittest

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
        self.assertEqual(expected, html)

    
    def test_bold_paragraph(self):
        md = """
**This is bolded paragraph
text in a p
tag here **

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><p><b>This is bolded paragraph text in a p tag here </b></p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
        self.assertEqual(expected, html)

    def test_heading(self):
        md = """
# Hello Heading h1

## Hello Heading h2

#### Hello Heading h4

###### Hello Heading h6
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(f"html: {html}")
        expected =  "<div><h1>Hello Heading h1</h1><h2>Hello Heading h2</h2><h4>Hello Heading h4</h4><h6>Hello Heading h6</h6></div>"
        self.assertEqual(expected, html)    

    def test_heading_inline_markdown(self):
        md = """
# **Hello** Heading h1

## _Hello_ Heading h2

#### `Hello` Heading h4

###### Hello ![Heading](h6)
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(f"html: {html}")
        expected =  "<div><h1><b>Hello</b> Heading h1</h1><h2><i>Hello</i> Heading h2</h2><h4><code>Hello</code> Heading h4</h4><h6>Hello <img src=\"h6\" alt=\"Heading\"></img></h6></div>"
        self.assertEqual(expected, html)  

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(f"html: {repr(html)}")
        expected ="<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"
        # print(f"expected: {repr(expected)}")
    
        self.assertEqual(html,expected)

    def test_codeblock_multiple(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```

```
**Bold code block, it should not change anything
second line of code block**
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(f"\n\nhtml: {repr(html)}\n")
        expected ="<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre><pre><code>**Bold code block, it should not change anything\nsecond line of code block**\n</code></pre></div>"
        # print(f"expected: {repr(expected)}")
    
        self.assertEqual(html,expected)
    
    def test_quoteblock(self):
        md = """
> Normal Quote
> **Bold** Quote
> _Italic_ Quote
>![image](quote)
>[link](quote)

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(f"\n\nhtml: {repr(html)}\n\n")
        expected = "<div><blockquote>Normal Quote <b>Bold</b> Quote <i>Italic</i> Quote <img src=\"quote\" alt=\"image\"></img><a href=\"quote\">link</a></blockquote></div>"
        # print(f"expected: {repr(expected)}")
    
        self.assertEqual(html,expected)

    def test_quoteblock_multiple(self):
        md = """
> Normal Quote
> **Bold** Quote
> _Italic_ Quote
>![image](quote)
>[link](quote)

>Second  
>Quote 
>block
>to
>test 
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(f"\n\nhtml: {repr(html)}\n\n")
        expected = "<div><blockquote>Normal Quote <b>Bold</b> Quote <i>Italic</i> Quote <img src=\"quote\" alt=\"image\"></img><a href=\"quote\">link</a></blockquote><blockquote>Second Quote block to test</blockquote></div>"
        # print(f"expected: {repr(expected)}")
    
        self.assertEqual(html,expected)
