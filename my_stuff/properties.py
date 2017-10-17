
a = 7

class C(object):
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x




c = C("bob")

print(c.x)

c.x ='John'

print(c.x)




def printA():
    print ("Value of a is %d" % (a))

def setA(value):
    global a
    a = value
    print ("Inside setA, a is now %d" %(a))


print ("Before setA")
printA()
setA(42)
print ("After setA")
printA()
