from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        old_nodes_split = node.text.split(delimiter)
        current_node_list = []

        if len(old_nodes_split) % 2 == 0:
            raise Exception("No delimiter found.")

        for i in range(len(old_nodes_split)):
            if old_nodes_split[i] == "":
                continue
            if i % 2 == 0:
                current_node_list.append(TextNode(old_nodes_split[i], text_type_text))
            else:
                current_node_list.append(TextNode(old_nodes_split[i], text_type))
        new_nodes.extend(current_node_list)
    return new_nodes

def extract_markdown_images(text):
    regex_extract_images = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return regex_extract_images

def extract_markdown_links(text):
    regex_extract_links = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return regex_extract_links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        old_nodes_split = node.text.split()