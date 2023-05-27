class Node :
    def __init__ (self,D,):
        self.data = D
        self.left = None
        self.right = None
class Tree:
    def __init__ (self):
        self.root = Node("i")
    def add(self,D,L):
        c = self.root
        b = c
        if L == "":
                c.data = D
        else:
            while len(L) > 1 :
                b = c
                f = str(L[0])
                if f == "L":
                    c = c.left
                    if c == None:
                        b.left = Node('i')
                        c = b.left
                elif f == "R":
                    c = c.right
                    if c == None:
                        b.right = Node('i')
                        c = b.right
                L = L[1:]
            b = c
            f = str(L[0])
            if f == "L":
                c = c.left
                if c == None:
                    b.left = Node('i')
                    c = b.left
            elif f == "R":
                c = c.right
                if c == None:
                    b.right = Node('i')
                    c = b.right
            if str(L[0]) == "L":
                if b.left == None and b.right == None:
                    b.left = Node(D)
                else:
                    b.left.data = D
            elif str(L[0]) == "R":
                if b.left == None and b.right == None:b.right = Node(D)
                else: c.data = D
    def BFS(self):
        if self.root == None : return
        Q = []
        Q.append(self.root)
        r = ''
        while len(Q)>0:
            P = Q.pop(0)
            r += P.data + " "
            if P.left != None : Q.append(P.left)
            if P.right != None : Q.append(P.right)
        r = r[:-1]
        if "i" in r:
            print("not complete")
        else:
            print(r)
while True:
    try:
        m = [None]
        e = True
        while m[-1] != "()":
            h = [h for h in input().split(" ") if h]
            if len(h) == 0:
                e = False
                break
            m +=h
        if e == False:break
        m = m[1:]
        a = True
        z = []
        w = Tree()
        for i in m:
            if i == "()" :break
            u = str(i)
            j = u.split(",")
            m1 = j[0][1:]
            m2 = j[1][:-1]
            if m2 in z:
                print("not complete")
                a = False
                break
            z.append(m2)
            w.add(m1,m2)
        if a == True:w.BFS()
    except:
        break