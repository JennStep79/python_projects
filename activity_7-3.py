# Binary search tree node class

class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

# node1 = BSTNode(3)
# print(node1) #3

# node2 = BSTNode(4, left=node1)
# print(node2) #4

# node3 = BSTNode()
# print(node3) #None
# node3.data = 5
# print(node3) #5

# Binary search tree class

class BST:
    def __init__(self, root=None):
        self.root = root
        self.contents = []

    def __str__(self):
        if self.root is None:
            return "The tree is empty"
        else:
            self.output = ''
            self.print_tree(node=self.root)
            return self.output

    def __repr__(self):
        if self.root is None:
            return "The tree is empty"
        else:
            self.output = ''
            self.print_tree(node=self.root)
            return self.output

    def print_tree(self, node, level=0):
        if node != None:
            self.print_tree(node.right, level + 1)
            self.output += ' ' * 4 * level + '-> ' + str(node.data) + '\n'
            self.print_tree(node.left, level + 1)

    def add(self, node):
        if type(node) != int and type(node) != BSTNode:
            raise ValueError("Node must be integer or BSTNode")


        if type(node) == int:
            node = BSTNode(node)

        if node in self.contents:
            return

        if self.root is None:
            self.root = node
            self.contents.append(node.data)
            return

        self.add_node(self.root, node)

        return

    def add_node(self, current_node, new_node):
        print(new_node.data, current_node.data)
        if new_node.data > current_node.data:
            if current_node.right is None:
                current_node.right = new_node
                self.contents.append(new_node.data)
                return
            else:
                self.add_node(current_node.right, new_node)
        else:
            if current_node.left is None:
                current_node.left = new_node
                self.contents.append(new_node.data)
                return
            else:
                self.add_node(current_node.left, new_node)

# bst = BST()
# print(bst)

# bst.root = node2
# print(bst)

# node2.right = node3
# print(bst)

#create tree from image
node8 = BSTNode(8)
node3 = BSTNode(3)
node10 = BSTNode(10)
node1 = BSTNode(1)
node6 = BSTNode(6)
node14 = BSTNode(14)
node4 = BSTNode(4)
node7 = BSTNode(7)
node13 = BSTNode(13)

bst = BST()
bst.add(node8)
bst.add(node3)
bst.add(node10)
bst.add(node1)
bst.add(node6)
bst.add(node14)
bst.add(node4)
bst.add(node7)
bst.add(node13)
print(bst)