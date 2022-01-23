class GrandParent:
    def __init__(self):
        self.lst = []


class Parent(GrandParent):
    def __init__(self):
        super(Parent, self).__init__()


class Child(Parent):
    def __init__(self):
        super(Child, self).__init__()
        