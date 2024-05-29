from textnode import TextNode



def main():
    test = TextNode("This is text node", "bold", "https://www.bootdev.com")

    print(test.__repr__)


if __name__ == "__main__":
    main()

