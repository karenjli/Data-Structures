# Import all the needed stacks including Doubly Linked List
from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('./dll_queue.py')
sys.path.append('./dll_stack.py')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Self is an object
        # Self.value is the value I am comparing to value

        # If self. value is greater than value
        if self.value > value:
            # Check the left node
            # If left node is None
            if self.left == None:
                # Left node will equal to the value
                self.left = BinarySearchTree(value)
            # If self.left is not empty
            else:
               # Run the insert function again
                self.left.insert(value)

        # If self.value is less than value
        elif self.value < value:
            # If right node is None
            if self.right == None:
                # Set self.right to value
                self.right = BinarySearchTree(value)
            else:
                # Run the insert function recursively
                # self.insert is needed to call the function within the object
                # insert by itself will not work
                self.right.insert(value)
        else:
            return ("Value equals to root")

    def contains(self, target):
        # If target == root, return
        if target == self.value:
            return True
        # else compare target with node
        else:
            # If target is greater than root
            if target > self.value:
                # If there is a value greater than root
                if self.right is not None:
                    # Run the contain function again
                    return self.right.contains(target)
                else:
                    # Return false if there are no value
                    return False

            # If target is smaller than root
            if target < self.value:
                # If there is a value smaller than root
                if self.left is not None:
                    # Run contain function again to test
                    return self.left.contains(target)
                else:
                    # Return false if there is no value
                    return False

    # Return the maximum value found in the tree

    def get_max(self):
        # Given the structure of the tree
        # Greatest number will be on furtherest and lowest right

        if self.right is not None:
            return self.right.get_max()
        # covers either root as the only value or the last value on the tree (leaf)
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # Check value on the right
        if self.right is not None:
            # If yes, loop again until the last value
            self.right.for_each(cb)
        # Check value on the left
        if self.left is not None:
            # If yes, loop again until last value
            self.left.for_each(cb)
        # Invoke call back function on the last value
        cb(self.value)

        # Below method fails the self.assertTrue (v3 in arr) test
        # base case - recursion stops when self.right and self.left == None
        # if self.right is None and self.left is None:
        #     return cb(self.value)
        # # while self.right or self.left
        # while self.right:
        #   # run cb function on current value

        #    # if self.right
        #     if self.right is not None:
        #         # run for each
        #         cb(self.value)
        #         return self.right.for_each(cb)

        #     # if self.left

        # while self.left:

        #     if self.left is not None:
        #         cb(self.value)
        #         # run for each
        #         return self.left.for_each(cb)
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # print one level at a time
        # go left if you can
        # go right if you can

        if self.left is not None:
            self.left.in_order_print(node)
        print(self.value)
        if self.right is not None:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        # queue set up
        queue = Queue()
        # Add value to tail of queue
        queue.enqueue(self)
        while queue.len() > 0:
            current_node = queue.dequeue()
            print(current_node.value)
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right is not None:
                queue.enqueue(current_node.right)

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
