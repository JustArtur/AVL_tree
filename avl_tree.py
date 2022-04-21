class Node:
    def __init__(self, value=None, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
        self.parent = None
        self.height = 1


class Tree:
    def __init__(self):
        self.root = None
        self.max_height = 0
        self.count = 0

    def insert(self, value):
        if self.root == None: self.root = Node(value)
        self._insert(value, self.root)

    def _insert(self, value, cur_node):
        # print(f"Insert {value}")
        if value == cur_node.value:
            print('This value already exist')  # not return, because recursion
            return
        elif value < cur_node.value:  # checking where to go
            print("Going left")
            if cur_node.left == None:
                self.count += 1
                cur_node.left = Node(value)
                cur_node.left.height += self.count
                self.max_height = max(self.max_height, cur_node.left.height)
                print("Linked node")
            else:
                print("Recursion")
                self._insert(value, cur_node.left)
        elif value > cur_node.value:  # checking where to go
            print("Going right")
            if cur_node.right == None:
                self.count += 1
                cur_node.right = Node(value)
                cur_node.right.height += self.count
                self.max_height = max(self.max_height, cur_node.right.height)
                print("Linked node")
            else:
                print("Recursion")
                self._insert(value, cur_node.right)

    def delete(self, value):
        cur_node = self.root
        while True:
            if value < cur_node.value:  # checking where to go
                print("Going left", cur_node.value)
                self._delete(value, cur_node.left)
            elif value > cur_node.value:  # checking where to go
                print("Going right", cur_node.value)
                self._delete(value, cur_node.right)

    # def _delete(self, value, cur_node):
    #     if value < cur_node.value:  # checking where to go
    #         print("Going left", cur_node.value)
    #         self.__delete(value, cur_node.left)
    #     elif value > cur_node.value:  # checking where to go
    #         print("Going right", cur_node.value)
    #         self.__delete(value, cur_node.right)

    def _delete(self, value, cur_node):
        if cur_node == None:
            print("Can't find value")
            return
        elif cur_node.value == value:
            print("Match")
            # If the node doesn't have a right and left subtree, then just cut it off and exit from the method
            if cur_node.left != None and cur_node.right != None:
                print("Deleting")
                cur_node = None
                return
            # If the node have a right and left subtree, then applying a special algorithm.
            elif cur_node.left != None and not cur_node.right != None:
                print("Swapping with both subtree")
                cur_node.value, cur_node.left.value = cur_node.left.value, cur_node.value
                return
                # If condition above fails, then we check for a left or right subtree
                # and simply reassign the links between the Nodes
            elif cur_node.left != None:  # Check for the left subtree
                print("Deleting")
                cur_node = cur_node.left
                return
            elif  cur_node.right != None:  # Check for the right subtree
                print("Deleting")
                cur_node = cur_node.right
        else:
            self._delete(value, cur_node)

    def find(self, value):
        cur_node = self.root
        while True:
            if cur_node == None: return False
            elif cur_node.value == value: return True
            elif value < cur_node.value:  # checking where to go
                # print("Going left", cur_node.value)
                cur_node = cur_node.left
                continue
            elif value > cur_node.value:  # checking where to go
                # print("Going right", cur_node.value)
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
t.insert(6)
t.insert(4)
t.insert(15)
t.insert(12)
t.insert(16)
t.insert(11)
t.insert(3)
# repr(t)
print(t.find(11))