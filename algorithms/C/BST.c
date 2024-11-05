#include <stdio.h>
#include <stdlib.h>

// Define the structure for a node in the BST
struct Node {
    int value;              // Value of the node
    struct Node *left;     // Pointer to the left child
    struct Node *right;    // Pointer to the right child
};

// Function to create a new node
struct Node* createNode(int value) {
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->value = value; // Set the value
    newNode->left = NULL;   // Initialize left child to NULL
    newNode->right = NULL;  // Initialize right child to NULL
    return newNode;
}

// Function to insert a value into the BST
struct Node* insert(struct Node *root, int value) {
    // If the tree is empty, return a new node
    if (root == NULL) {
        return createNode(value);
    }

    // Otherwise, recur down the tree
    if (value < root->value) {
        root->left = insert(root->left, value); // Use z->left
    } else if (value > root->value) {
        root->right = insert(root->right, value); // Use z->right
    }

    // Return the unchanged root pointer
    return root;
}

// Function to perform inorder traversal of the BST
void inorder(struct Node *root) {
    if (root != NULL) {
        inorder(root->left); // Visit left subtree
        printf("%d ", root->value); // Visit node
        inorder(root->right); // Visit right subtree
    }
}

// Function to search for a value in the BST
struct Node* search(struct Node *root, int value) {
    // Base case: root is null or value is present at root
    if (root == NULL || root->value == value) {
        return root;
    }

    // Value is greater than root's value
    if (value > root->value) {
        return search(root->right, value); // Use z->right
    }

    // Value is smaller than root's value
    return search(root->left, value); // Use z->left
}

// Main function to demonstrate the BST
int main() {
    struct Node *root = NULL; // Initialize the root of the BST

    // Insert values into the BST
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);

    // Print the inorder traversal of the BST
    printf("Inorder Traversal: ");
    inorder(root);
    printf("\n");

    // Search for a value in the BST
    int searchValue = 40;
    struct Node *foundNode = search(root, searchValue);
    if (foundNode != NULL) {
        printf("Value %d found in the BST.\n", searchValue);
    } else {
        printf("Value %d not found in the BST.\n", searchValue);
    }

    // Free allocated memory (not shown for simplicity)
    // In a real application, you should implement a function to free the tree.

    return 0;
}