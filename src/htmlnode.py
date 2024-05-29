class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Function yet to be implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        
        return f' href="{self.href}" target={self.target}'

    def __repr__(self):
        return f'{self.tag}, {self.value}, {self.children}, {self.props}'
