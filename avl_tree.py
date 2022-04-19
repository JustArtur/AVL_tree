class Node:
    def __init__(self, value=None, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
        self.parent = None
        self.height = 1


class Tree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, value):
        cur_node = self.root
        self._insert(value, cur_node)

    def _insert(self, value, cur_node):
        #print(f"Insert {value}")
        if value == cur_node.value:
            print('This value already exist')  # not return, because recursion
            return
        elif value < cur_node.value:  # checking where to go
            print("Going left")
            if cur_node.left == None:
                cur_node.left = Node(value)
                print("Linked node")
            else:
                print("Recursion")
                self._insert(value, cur_node.left)
        elif value > cur_node.value:  # checking where to go
            print("Going right")
            if cur_node.right == None:
                cur_node.right = Node(value)
                print("Linked node")
            else:
                print("Recursion")
                self._insert(value, cur_node.right)

    def delete(self, value):
        cur_node = self.root
        self._delete(value, cur_node)

    def _delete(self, value, cur_node):
        if value < cur_node.value:  # checking where to go
            print("Going left", cur_node.value)
            if cur_node.left is None:
                print("Can't find value")
                return
            elif cur_node.left.value == value:
                print("Match")
                # If the node doesn't have a right and left subtree, then just cut it off and exit from the method
                if (cur_node.left.left is None) and (cur_node.left.right is None):
                    print("Deleting")
                    cur_node.right = None
                    return
                # If the node have a right and left subtree, then applying a special algorithm.
                elif not (cur_node.left.left is None) and not (cur_node.left.right is None):
                    print("Swapping with both subtree")
                    cur_node.left.value, cur_node.left.left.value = cur_node.left.left.value, cur_node.left.value
                    return
                    # If condition above fails, then we check for a left or right subtree
                    # and simply reassign the links between the Nodes
                elif not (cur_node.left.left is None):  # Check for the left subtree
                    print("Deleting")
                    cur_node.left = cur_node.left.left
                    return
                elif not (cur_node.left.right is None):  # Check for the right subtree
                    print("Deleting")
                    cur_node.left = cur_node.left.right
            else:
                self._delete(value, cur_node.left)
        if value > cur_node.value:   # checking where to go
            print("Going right", cur_node.value)
            if cur_node.right is None:
                print("Can't find value")
                return
            elif cur_node.right.value == value:
                # If the node doesn't have a right and left subtree, then just cut it off and exit from the method
                if cur_node.right.left is None and cur_node.right.right is None:
                    cur_node.right = None
                    return
                # If the node have a right and left subtree, then applying a special algorithm.
                elif not (cur_node.right.left is None) and not (cur_node.right.right is None):
                    cur_node.right.value, cur_node.right.left.value = cur_node.right.left.value,cur_node.right.value
                    return
                    # If condition above fails, then we check for a left or right subtree
                    # and simply reassign the links between the Nodes
                elif not (cur_node.right.left is None):    # Check for the left subtree
                    print("Deleting")
                    cur_node.right = cur_node.right.left
                    return
                elif not (cur_node.right.right is None):    # Check for the right subtree
                    print("Deleting")
                    cur_node.right = cur_node.right.right
            else:
                self._delete(value, cur_node.right)

    def find(self, value):
        pass

    def __repr__(self):
        pass


t = Tree(10)
t.insert(5)
t.insert(6)
t.insert(15)
t.insert(12)

print(t.root.right.value)
t.delete(15)
print(t.root.right.value)





