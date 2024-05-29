import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        htmlnode = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})

        actual = htmlnode.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'
        
        self.assertEqual(actual, expected)



if __name__ == "__main__":
    unittest.main()