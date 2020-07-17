class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        if find_val < self.root.value:
            if self.left is None:
                return False
            return self.left.serach(find_val)
        elif find_val > self.root.value:
            if self.right is None:
                return False
            return self.right.findval(find_val)
        else:
            return self.root.value

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        # Your code goes here
        pass

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        # Your code goes here
        pass

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        # Your code goes here
        pass

    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    print(tree.search(4))