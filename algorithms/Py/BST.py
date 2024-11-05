class Node:
    def __init__(self, value):
        self.value = value  # Set the value of the node
        self.left = None    # Initialize left child to None
        self.right = None   # Initialize right child to None

class BinarySearchTree:
    def __init__(self):
        self.root = None  # Initialize the root of the BST

    def insert(self, value):
        """Insert a new value into the BST."""
        if self.root is None:
            self.root = Node(value)  # If the tree is empty, create the root node
        else:
            self._insert_recursively(self.root, value)  # Call the recursive insert function

    def _insert_recursively(self, node, value):
        """Helper method to insert a value recursively."""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)  # Insert as left child
            else:
                self._insert_recursively(node.left, value)  # Recur down the left subtree
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)  # Insert as right child
            else:
                self._insert_recursively(node.right, value)  # Recur down the right subtree

    def inorder(self):
        """Perform inorder traversal of the BST."""
        return self._inorder_recursively(self.root)

    def _inorder_recursively(self, node):
        """Helper method for inorder traversal."""
        result = []
        if node is not None:
            result.extend(self._inorder_recursively(node.left))  # Visit left subtree
            result.append(node.value)  # Visit node
            result.extend(self._inorder_recursively(node.right))  # Visit right subtree
        return result

    def search(self, value):
        """Search for a value in the BST."""
        return self._search_recursively(self.root, value)

    def _search_recursively(self, node, value):
        """Helper method to search for a value recursively."""
        if node is None or node.value == value:
            return node  # Return the node if found or None if not found
        if value < node.value:
            return self._search_recursively(node.left, value)  # Search in the left subtree
        return self._search_recursively(node.right, value)  # Search in the right subtree

# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    
    # Insert values into the BST
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    # Print the inorder traversal of the BST
    print("Inorder Traversal:", bst.inorder())  # Output: Inorder Traversal: [20, 30, 40, 50, 60, 70, 80]

    # Search for a value in the BST
    search_value = 40
    found_node = bst.search(search_value)
    if found_node:
        print(f"Value {search_value} found in the BST.")
    else:
        print(f"Value {search_value} not found in the BST.")