
class node:
    def __init__(self, data=None):
        self.data = data
        self.nodes = []
        self.parent = None

class ifNode (node):
    def __init__(self, condition):
        super().__init__(condition)
        self.branch = None
        self.left = []
        self.right = []