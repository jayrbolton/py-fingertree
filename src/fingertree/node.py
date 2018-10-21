
class Node:

    def __init__(self):
        self.size = 0
        self.hasThree = False

    def get(self, idx):
        if idx == 0:
            return self.a
        if idx == 1:
            return self.b
        else:
            return self.c
