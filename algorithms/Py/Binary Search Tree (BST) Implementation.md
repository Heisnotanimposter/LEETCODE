# Binary Search Tree (BST) Implementation

This repository contains implementations of a Binary Search Tree (BST) in both C and Python. This document highlights the differences between accessing members of a structure in C using the arrow (`->`) notation and accessing attributes in Python using dot (`.`) notation.

## Overview of Notations

### C Notation: Arrow (`->`)

In C, when you have a pointer to a structure, you use the arrow operator (`->`) to access the members of that structure. This operator dereferences the pointer and accesses the specified member in one step.

#### Example in C

c
#include <stdio.h>
#include <stdlib.h>
// Define the structure for a node in the BST
struct Node {
int value; // Value of the node
struct Node left; // Pointer to the left child
struct Node right; // Pointer to the right child
};
// Function to create a new node
struct Node createNode(int value) {
struct Node newNode = (struct Node )malloc(sizeof(struct Node));
newNode->value = value; // Accessing the 'value' member using z->value
newNode->left = NULL; // Initialize left child to NULL
newNode->right = NULL; // Initialize right child to NULL
return newNode;
}


In this example, `newNode->value` accesses the `value` member of the `Node` structure that `newNode` points to.

### Python Notation: Dot (`.`)

In Python, you use dot notation (`.`) to access attributes of an object. This is a straightforward way to access properties and methods of a class instance.

#### Example in Python

python
class Node:
def init(self, value):
self.value = value # Set the value of the node
self.left = None # Initialize left child to None
self.right = None # Initialize right child to None
Create an instance of Node
z = Node(10)
Access the 'value' attribute using dot notation
print("Value:", z.value) # Output: Value: 10

In this example, `z.value` accesses the `value` attribute of the `Node` instance `z`.

## Key Differences

| Feature                | C (`->` Notation)                     | Python (`.` Notation)                |
|------------------------|---------------------------------------|--------------------------------------|
| **Usage**              | Used with pointers to structures      | Used with instances of classes       |
| **Syntax**             | `pointer->member`                     | `object.member`                      |
| **Dereferencing**      | Automatically dereferences the pointer| No need for explicit dereferencing   |
| **Type Safety**        | Requires explicit type definitions     | Dynamically typed, more flexible     |

## Conclusion

Understanding the differences between C's arrow notation and Python's dot notation is crucial for effectively working with data structures in both languages. While C requires explicit pointer management, Python's object-oriented approach simplifies member access through dot notation.

Feel free to explore the implementations in this repository and see how these notations are applied in the context of a Binary Search Tree.