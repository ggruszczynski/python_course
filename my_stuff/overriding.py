

class A(object):
    def __method(self):
        print("I'm a method in A")

    def method(self):
        self.__method()


class B(A):
    def __method(self):
        print("I'm a method in B")


a = A()
a.method()

b = B()
b.method()