# Define a tree

class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def insert(self, data):
        if (self.data is None):   # Check Head
            self.data = data
        else:
            if (data < self.data):
                #  Check the node  if nothing on the left insert the node of the with value data
                if (self.left is None):
                    self.data = Node(data)
                else:
                    self.left.insert(data)  # Recursion
             #  Check the node  if nothing on the right insert the node of the with value data
            elif (data > self.right):
                if (self.right == None):
                    self.right = Node(data)
                else:
                    self.right.insert(data)



if __name__== '__main__':
    print("Welcome to Tree Data Structure")
    root = Node('g')
    root.insert('c')
    root.insert('b')
    root.insert('a')
    root.insert('e')
    root.insert('d')
    root.insert('f')
    root.insert('i')
    root.insert('h')
    root.insert('j')
    root.insert('k')