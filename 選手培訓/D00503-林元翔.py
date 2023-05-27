class Node :
    def __init__ (self,D):
        self.data = D
        self.left = None
        self.right = None
        self.mid = None
class Tree:
    def __init__ (self):
        self.root = None
    def add(self,D):
        N = Node(D)
        if self.root == None:
            self.root = N
            N.mid = '-'
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
                b.left.mid = b.data
            else:
                b.right = Node(D)
                b.right.mid = b.data
    def intraversal(self,p):
        if p == None:return
        self.intraversal(p.left)
        y = p.mid
        if y == None:y = '-'
        print(f"{p.data} {y}")
        self.intraversal(p.right)
    def inorder(self):
        self.intraversal(self.root)
while True:
    try:
        m = input().split(' ')
        if len(m) == 0:break
        w = Tree()
        for i in range(len(m)):
            w.add(eval(m[i]))
        w.inorder()
    except:
        break