from src.utilities.extract_markdown_images import extract_markdown_images
import unittest

class TestExtractMarkDownImage(unittest.TestCase):
  def test_extracting_one_image(self):
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
    expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
    self.assertEqual(expected, extract_markdown_images(text))
  
  def test_extracting_multiples_images(self):
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif), ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg), and ![TOP](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.freecodecamp.org%2Fespanol%2Fnews%2Fcontent%2Fimages%2Fsize%2Fw2000%2F2024%2F01%2FThe-Odin-Project.png&f=1&nofb=1&ipt=9061a4952e14d5b9833df312e5555e989ad8f62325cb7af945bfefd6016a17c6)"

    expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"), ("TOP","https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.freecodecamp.org%2Fespanol%2Fnews%2Fcontent%2Fimages%2Fsize%2Fw2000%2F2024%2F01%2FThe-Odin-Project.png&f=1&nofb=1&ipt=9061a4952e14d5b9833df312e5555e989ad8f62325cb7af945bfefd6016a17c6" )]

    self.assertEqual(expected, extract_markdown_images(text))
  
  def test_extracting_image_with_altText(self):
    text = "This is a text with a (image link but no alt text)"

    with self.assertRaises(Exception):
      extract_markdown_images(text)
  
  def test_extracting_image_with_no_url(self):
    text = "This is a text with a ![no url]"
    with self.assertRaises(Exception):
      extract_markdown_images(text)

  def test_extracting_a_normal_text(self):
    text = "This is a text with no image"
    expected = []
    self.assertEqual(expected, extract_markdown_images(text))

  def test_extracting_image_at_beginning(self):
    text = "![obi wan](https://i.imgur.com/aKaOqIh.gif) says hello"
    expected = [("obi wan", "https://i.imgur.com/aKaOqIh.gif")]
    self.assertEqual(expected, extract_markdown_images(text))