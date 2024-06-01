import unittest

from inline_markdown import ( 
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_single_node_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        
        expected = [TextNode("This is text with a ", text_type_text),TextNode("code block", text_type_code),TextNode(" word", text_type_text),]
        actual = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(expected, actual)
    
    def test_single_node_bold(self):
        node = TextNode("This is text with a **bold** word", text_type_text)
        
        expected = [TextNode("This is text with a ", text_type_text),TextNode("bold", text_type_bold),TextNode(" word", text_type_text),]
        actual = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertEqual(expected, actual)

    def test_single_node_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        
        expected = [TextNode("This is text with an ", text_type_text),TextNode("italic", text_type_italic),TextNode(" word", text_type_text),]
        actual = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertEqual(expected, actual)

    def test_test(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"

        expected = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        actual = extract_markdown_links(text)
        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()