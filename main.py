from copy import deepcopy


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:

    def __init__(self):
        self.root = Node(23)

    def call_method(self, key, arg=None):
        if key == 0:
            self.insert(arg)
        elif key == 1:
            self.inorder_traversal()
            print()
        elif key == 2:
            self.preorder_traversal()
            print()
        elif key == 3:
            self.postorder_traversal()
            print()
        elif key == 4:
            print(self.get_height())
        elif key == 5:
            found = self.inorder_search(arg)
            print('true' if found else 'false')
        elif key == 6:
            self.mirror()

    def insert(self, value):
        node = Node(value)
        self.insert_recursive(self.root, node)

    def inorder_traversal(self):
        self.inorder_traversal_recursive(self.root)

    def preorder_traversal(self):
        self.preorder_traversal_recursive(self.root)

    def postorder_traversal(self):
        self.postorder_traversal_recursive(self.root)

    def get_height(self):
        return self.get_height_recursive(self.root)

    def inorder_search(self, key):
        return self.inorder_search_recursive(self.root, key)

    def mirror(self):
        new_root = deepcopy(self.root)
        return self.mirror_recursive(new_root)

    @staticmethod
    def insert_recursive(root, node):
        if node.data <= root.data:
            if root.left is None:
                root.left = node
                return
            else:
                BinarySearchTree.insert_recursive(root.left, node)
        else:
            if root.right is None:
                root.right = node
                return
            else:
                BinarySearchTree.insert_recursive(root.right, node)

    @staticmethod
    def inorder_traversal_recursive(node):
        if node is not None:
            BinarySearchTree.inorder_traversal_recursive(node.left)
            print(node, end='\t')
            BinarySearchTree.inorder_traversal_recursive(node.right)

    @staticmethod
    def preorder_traversal_recursive(node):
        if node is not None:
            print(node, end='\t')
            BinarySearchTree.preorder_traversal_recursive(node.left)
            BinarySearchTree.preorder_traversal_recursive(node.right)

    @staticmethod
    def postorder_traversal_recursive(node):
        if node is not None:
            BinarySearchTree.postorder_traversal_recursive(node.left)
            BinarySearchTree.postorder_traversal_recursive(node.right)
            print(node, end='\t')

    @staticmethod
    def get_height_recursive(node):
        if node is None:
            return 0
        return 1 + max(BinarySearchTree.get_height_recursive(node.left),
                       BinarySearchTree.get_height_recursive(node.right))

    @staticmethod
    def inorder_search_recursive(node, key):
        if key == node.data:
            return Node(key)
        if key > node.data:
            if node.right is None:
                return None
            return BinarySearchTree.inorder_search_recursive(node.right, key)
        if node.left is None:
            return None
        return BinarySearchTree.inorder_search_recursive(node.left, key)

    @staticmethod
    def mirror_recursive(node):
        if node is not None:
            if node.left is not None:
                BinarySearchTree.mirror_recursive(node.left)
            if node.right is not None:
                BinarySearchTree.mirror_recursive(node.right)
            node.left, node.right = node.right, node.left

        return node


if __name__ == '__main__':

    n = int(input())
    bst = BinarySearchTree()
    inputs = []
    for _ in range(n):
        inputs.append(map(int, input().split()))

    for input_data in inputs:
        bst.call_method(*input_data)
