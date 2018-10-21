

class Affix:

    def __init__(self):
        self.length = 0
        pass


    def to_array(self):
        if self.length == 0:
            return []
        if self.length == 1:
            return [self.a]
        if self.length == 2:
            return [self.a, self.b]
        if self.length == 3:
            return [self.a, self.b, self.c]
        if self.length == 4:
            return [self.a, self.b, self.c, self.d]

    def get(self, idx):
        if idx == 0:
            return self.a
        if idx == 1:
            return self.b
        if idx == 2:
            return self.c
        if idx == 3:
            return self.d
