class Stack:
    def __init__(self):
        self.s = []
    def add(self, node):
        self.s.append(node)
    def get(self):
        node = self.s[len(self.s)-1]
        self.s = self.s[:len(self.s)-1]
        return node
    def isempty(self):
        if len(self.s) == 0:
            return True
        return False
    def display(self):
        print("items in stack: ", end="")
        for item in self.s:
            print(item, end="  ")
        print("")