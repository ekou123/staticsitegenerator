import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "italics", "www.google.com")
        node2 = TextNode("This is a text node", "Bold", "www.google.com")

        self.assertNotEqual(node, node2)

    def not_assessed(self):
        node = TextNode("This is a text node with a `code block` word", text_type_text)

        
        expected = ["This is a text node with a ", "code block", " word"]
        actual = split_nodes_delimiter([node], "`", )
            


if __name__ == "__main__":
    unittest.main()