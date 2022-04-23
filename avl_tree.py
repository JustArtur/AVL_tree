class Node:
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.value = value
        self.parent = parent


class Tree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return self.value

    def insert(self, value):
        # init the tree
        if self.root == None:
            self.root = Node(value)
            return
        self._insert(value, self.root)

    def _insert(self, value, cur_node):
        # if the value is already exist, then just return
        if value == cur_node.value:
            return
        # Checking where to go right or left
        elif value < cur_node.value:
            if cur_node.left == None:
                cur_node.left = Node(value)
                cur_node.left.parent = cur_node
            else:
                self._insert(value, cur_node.left)
        else:
            if cur_node.right == None:
                cur_node.right = Node(value)
                cur_node.right.parent = cur_node
            else:
                self._insert(value, cur_node.right)

    def delete(self, value):
        self._delete(self.find(value))

    def _delete(self, cur_node):
        # return the rightmost node of left child
        def __get_rightmost_node(node):
            while node.right != None:
                node = node.right
            return node

        def __delete_successor(node):
            pass

        # If the node doesn't have a right and left subtree, then just cut it off and exit from the method
        if cur_node.left == None and cur_node.right == None:
            if cur_node.parent.left == cur_node:
                cur_node.parent.left = None
            else:
                cur_node.parent.right = None
            print("Deleting", 'all none')

        # If the node have a right and left subtree, then applying a special algorithm.
        elif cur_node.left != None and cur_node.right != None:
            print("Both subtree")
            right_node = __get_rightmost_node(cur_node.left)
            cur_node.value = right_node.value
            parent_node = right_node.parent
            if parent_node.left == right_node:
                parent_node.left = None
            else:
                parent_node.right = None


            # If condition above fails, then we check for a left or right subtree
            # and simply reassign the links between the Nodes
        elif cur_node.left != None:
            print("Deleting")
            if cur_node.parent.left == cur_node:
                cur_node.parent.left = cur_node.left
            else:
                cur_node.parent.right = cur_node.left
        else:
            print("Deleting")
            if cur_node.parent.left == cur_node:
                cur_node.parent.left = cur_node.right
            else:
                cur_node.parent.right = cur_node.right
            cur_node.parent = cur_node.right

    def find(self, value):
        cur_node = self.root
        while True:
            if cur_node == None:
                return False
            # if value is equal, then return True
            elif cur_node.value == value:
                return cur_node
            # Checking where to go right or left
            elif value < cur_node.value:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right


    def left_rotate(self):
         pass

    def right_rotate(self):
        pass

    # def __repr__(self):
    #     cur_nodes = [self.root]
    #     next_nodes = []
    #     space = '   '
    #     none_node = '   '
    #     row = ' ' * (self.max_height * 2 - 6)
    #
    #     while True:
    #         if all(n == None for n in cur_nodes): break
    #         for n in cur_nodes:
    #             if n == None:
    #                 row = row + space
    #                 continue
    #             next_nodes.append(n.left)
    #             next_nodes.append(n.right)
    #
    #             if n == None:
    #                 row = row + space
    #             else:
    #                 row = row + str(n.value) + space
    #         print(row)
    #         cur_nodes = next_nodes.copy()
    #         row = ' ' * int((self.max_height * 2) / next_nodes[0].height)
    #         next_nodes = []


t = Tree()
t.insert(10)
t.insert(5)
t.insert(2)
t.insert(3)
t.insert(4)
t.insert(6)
t.delete(5)
print(t.find(5))
