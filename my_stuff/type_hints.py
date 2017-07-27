
class Person(object):
    """docstring for ClassName"""

    def __init__(self, name: str):
        # super(Klasa, self).__init__()
        self.name = name
        self.weight = 123


def greeting(someone: Person) -> str:
    return 'Hello ' + someone.name


def greeting_plain(someone):
    return 'Hello ' + someone.name


def greeting2(name: str) -> str:
    return 'Hello ' + name

person = Person("John")
elo = greeting(person)
print(elo)
