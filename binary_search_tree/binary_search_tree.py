import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # inserted = False
        # while not inserted:
        #     if value < self.value:
        #         if self.left is None:
        #             self.left = BinarySearchTree(value)
        #             inserted = True
        #         else:
        #             self = self.left
        #     elif value > self.value:
        #         if self.right is None:
        #             self.right = BinarySearchTree(value)
        #             inserted = True
        #         else:
        #             self = self.right
        #     else:
        #         break

        # return inserted
        cur = self
        left = value < cur.value
        while (nxt := cur.left if value < cur.value else cur.right) is not None:
            cur = next
            
            
        node = BinarySearchTree(value)
        if left:
            cur.left = node
        else:
            cur.right = node

        # refactor
        cur = self
        left = value < cur.value
        nxt = cur.left if value < cur.value else cur.right
        while nxt is not None:
            cur = next
            nxt = cur.left if value < cur.value else cur.right

        go_left = value < cur.value
        node = BinarySearchTree(value)
        if left:
            cur.left = node
        else:
            cur.right = node
        


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        while self:
            if self.value == target:
                return True

            if target < self.value:
                self = self.left
            elif target > self.value:
                self = self.right

        return False

        # # first version
        # while True:
        #     if target == self.value:
        #         return True
        #     elif target < self.value:
        #         if self.left:
        #             self = self.left
        #         else:
        #             return False
        #     elif target > self.value:
        #         if self.right:
        #             self = self.right
        #         else:
        #             return False
            

    # Return the maximum value found in the tree
    def get_max(self):
        while self.right:
            self = self.right
        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    # recursive
    # def for_each(self, cb):
    #     cb(self.value)
    #     if self.left:
    #         self.left.for_each(cb)
    #     if self.right:
    #         self.right.for_each(cb)

    # iterative
    def for_each(self, cb):
        stack = Stack()
        stack.push(self)
        # while stack is not empty
        while stack.size > 0:
            # pop node from stack
            popped = stack.pop()
            # pass noce value to cb
            cb(popped.value)
            # push children to stack
            if popped.left:
                stack.push(popped.left)
            if popped.right:
                stack.push(popped.right)
            
    

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)
        print(self.value)
        # collected.append(self.value)
        
        if self.right:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

# collected = []

# bst = BinarySearchTree(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.in_order_print(bst)

# for item in collected:
#     print(type(item), item)