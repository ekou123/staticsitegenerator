import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_htmlnode(self):
        htmlnode = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})

        actual = htmlnode.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'
        
        self.assertEqual(actual, expected)

    def test_to_html_required_values_only_leafnode(self):
        leafnode = LeafNode("p", "This is a paragraph of text.")

        expected = '<p>This is a paragraph of text.</p>'
        actual = leafnode.to_html()

        self.assertEqual(expected, actual)
    
    def test_to_html_all_values_leafnode(self):
        leafnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        expected = '<a href="https://www.google.com">Click me!</a>'
        actual = leafnode.to_html()

        self.assertEqual(expected, actual)

    def test_to_html_parent_node(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ],
                )

        expected = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        actual = node.to_html()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()