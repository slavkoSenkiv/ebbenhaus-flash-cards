class Parent:
    def __init__(self):
        self.dic1 = {'a': 1, 'b': 2}

    def dic_print(self):
        print(f'the dic is {self.dic1}')


class Child(Parent):
    def __init__(self):
        self.dic1 = {'c': 3, 'd': 4}


Parent().dic_print()
Child().dic_print()