
class A(object):
    a = 'a'

    def __init__(self):
        self.selfa = 'selfa'
    # def __init__(self, x):
    #     self._x = x
    #
    # @property
    # def x(self):
    #     """I'm the 'x' property."""
    #     return self._x
    #
    # @x.setter
    # def x(self, value):
    #     self._x = value
    #
    # @x.deleter
    # def x(self):
    #     del self._x


class B(A):
    a = 'b'

    def __init__(self):
        self.selfa = 'selfb'


class C(A):
    a = 'c'

    def __init__(self):
        self.selfa = 'selfc'



xa = A()

xb = B()

A.a = 'another_stuff_a'
A.selfa = 'oups_a'

B.a = 'another_stuff_b'
B.selfa = 'oups_b'

print('wyszlo %r', xa)