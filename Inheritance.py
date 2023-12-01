from OOPS import Calculator


class ChildClass(Calculator):
    n2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def get_all_data(self):
        return ChildClass.n2 + self.n + self.summ()


obj3 = ChildClass()
print(obj3.get_all_data())
