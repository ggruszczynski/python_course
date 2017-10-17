

class Person(object):
    """docstring for ClassName"""

    def __init__(self, name='bob'):
        # super(Klasa, self).__init__()
        self.name = name
        self.weight = 123


def greeting(someone = Person) -> str:
    # someone.nazwa = 'jas'
    result = 'Hello ' + someone.name
    return result


def greeting_plain(someone = Person()):
    result = 'Hello ' + someone.name
    return result

# def greeting2(name: str) -> str:
#     return 'Hello ' + name

person = Person("John")


elo_plain = greeting_plain()
print(elo_plain)

elo = greeting()
print(elo)