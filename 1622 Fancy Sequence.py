class Fancy:
    def __init__(self):
        self.MOD = 1000000007
        self.vals = []
        self.a = 1
        self.b = 0

    def append(self, val: int) -> None:
        x = (val - self.b + self.MOD) % self.MOD
        self.vals.append(x * pow(self.a, self.MOD - 2, self.MOD) % self.MOD)

    def addAll(self, inc: int) -> None:
        self.b = (self.b + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.a = (self.a * m) % self.MOD
        self.b = (self.b * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.vals):
            return -1
        return (self.a * self.vals[idx] + self.b) % self.MOD
