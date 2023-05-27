class Node :
    def __init__ (self,D):
        self.data = D
        self.left = None
        self.right = None
class Tree:
    def __init__ (self):
        self.root = None
    def add(self,D):
        N = Node(D)
        if self.root == None:
            self.root = N
        else:
            c = self.root
            while c != None:
                b = c
                if c.data > D:
                    c = c.left 
                else:
                    c = c.right 
            if b.data > D:
                b.left = Node(D)
            else:
                b.right = Node(D)