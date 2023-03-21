# 1.Implement Binary tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if val < node.val:
            if not node.left:
                node.left = TreeNode(val)
            else:
                self._insert(val, node.left)
        else:
            if not node.right:
                node.right = TreeNode(val)
            else:
                self._insert(val, node.right)

    def search(self, val):
        return self._search(val, self.root)

    def _search(self, val, node):
        if not node or node.val == val:
            return node
        elif val < node.val:
            return self._search(val, node.left)
        else:
            return self._search(val, node.right)


# 2.Find height of a given tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_height(root):
    if root is None:
        return 0
    else:
        left_height = tree_height(root.left)
        right_height = tree_height(root.right)
        return max(left_height, right_height) + 1

# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Find the height of the tree
height = tree_height(root)
print(height)  # Output: 3



# 3.Perform Pre-order, Post-order, In-order traversal

# Node class for a binary tree
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Pre-order traversal
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

# In-order traversal
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

# Post-order traversal
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Pre-order traversal:")
preorder(root)

print("\nIn-order traversal:")
inorder(root)

print("\nPost-order traversal:")
postorder(root)


# 4.Function to print all the leaves in a given binary tree

def print_leaves(root):
    if root is not None:
        if root.left is None and root.right is None:
            print(root.val)  # print leaf node
        else:
            print_leaves(root.left)
            print_leaves(root.right)


# 5.Implement BFS (Breath First Search) and DFS (Depth First Search)

from collections import deque

def bfs(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def dfs(root):
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


# 6.Find sum of all left leaves in a given Binary Tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_left_leaves(root):
    if root is None:
        return 0
    
    if root.left is not None and root.left.left is None and root.left.right is None:
        return root.left.value + sum_left_leaves(root.right)
    
    return sum_left_leaves(root.left) + sum_left_leaves(root.right)


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)

print(sum_left_leaves(root)) # Output: 15

# 7.Find sum of all nodes of the given perfect binary tree

import math

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def perfectBinaryTreeSum(root):
    
    h = math.floor(math.log2(countNodes(root)+1))
    
    nodes = 2**(h+1) - 1
    
    return nodes * (nodes + 1) // 2

def countNodes(root):
    if root is None:
        return 0
    else:
        return 1 + countNodes(root.left) + countNodes(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(perfectBinaryTreeSum(root)) 

# 8.Count subtress that sum up to a given value x in a binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def count_subtrees(node, x):
    if node is None:
        return 0
    
    left_sum = count_subtrees(node.left, x)
    right_sum = count_subtrees(node.right, x)
    
    subtree_sum = node.data + left_sum + right_sum
    
    if subtree_sum == x:
        return 1 + left_sum + right_sum
    
    return left_sum + right_sum
    

root = Node(5)
root.left = Node(3)
root.right = Node(1)
root.left.left = Node(-2)
root.left.right = Node(4)
root.right.left = Node(-1)
root.right.right = Node(2)

x = 2
print(count_subtrees(root, x))  

# 9.Find maximum level sum in Binary Tree


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxLevelSum(root):
    if not root:
        return 0
        
    queue = [root]
    max_sum = float('-inf')
    
    while queue:
        level_sum = 0
        level_size = len(queue)
        
        for i in range(level_size):
            curr_node = queue.pop(0)
            level_sum += curr_node.val
            
            if curr_node.left:
                queue.append(curr_node.left)
            
            if curr_node.right:
                queue.append(curr_node.right)
        
        max_sum = max(max_sum, level_sum)
        
    return max_sum


# 10.Print the nodes at odd levels of a tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_odd_level_nodes(root):
    if root is None:
        return

    
    queue = []
    queue.append(root)
    level = 1

    while len(queue) > 0:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.pop(0)

            if level % 2 == 1:
                print(node.val, end=' ')

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        level += 1




