# Representation for General Trees

class Tree(object):
    def __init__(self, entry, less=None, right=None):
        self.entry
        self.left = left
        self.right = right

    @property
    def is_leaf(self):
        return not self.left and not self.right


