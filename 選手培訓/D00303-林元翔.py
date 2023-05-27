class RecentCounter:
    def __init__(self):
        self.z = []
        r = 1
    def ping(self, t: int) -> int:
        self.z.append(t)
        self.t1 = t-3000
        for i in self.z:
            if i < self.t1:
                self.z = self.z[1:]
            else:break
        return len(self.z)
while True:
    try:
        Q = RecentCounter()
        A = []
        for d in [int(_) for _ in input().split(",") if _] :
            A.append(Q.ping(d))
        if len(A)>0 : print(A)
        else : break
    except:
        break