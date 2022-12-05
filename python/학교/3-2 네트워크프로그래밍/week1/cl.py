class Score:
    def __init__(self, p=0):
        self.point = p
    def set(self, p):
        self.point = p
    def get(self):
        return self.point

obj = Score()
print(obj.get())
obj.set(95)
print(obj.get())
