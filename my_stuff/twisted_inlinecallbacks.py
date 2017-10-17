from twisted.internet import defer
from twisted.python import failure, util
from twisted.internet import defer, reactor
from twisted.internet import defer
from twisted.web import client
from twisted.internet import reactor
import sys


def doubleResult(res1):
    return 2 * res1

def printResult(res2):
    print(res2)
    return res2

def doubleAndPrint1():
    d = defer.Deferred() # getDeferredFromSomewhere()

    d.addCallback(doubleResult)
    d.addCallback(printResult)
    return d


d1 = doubleAndPrint1()
d1.callback("elo ")



def get_some_string(str):
    return "hoho " + str

def deferredExample():
    d = defer.Deferred()
    d.addCallback(get_some_string)
    d.callback("cos")

    return d


@defer.inlineCallbacks
def doubleAndPrint2():
    res1 = yield deferredExample() # getDeferredFromSomewhere()
    res2 = res1 * 2

    defer.returnValue(res2)



d2 = doubleAndPrint2()

d2.addCallback(printResult)

x = 5
print(d2.result)


#
# @defer.inlineCallbacks
# def enqueueTaskToDisplayURL(url):
#     try:
#         data = yield client.getPage(url)
#         print(data)
#     except Exception as e:
#         print("Error: %s", e)
#         return
#     finally:
#         reactor.stop()
#
# if __name__ == "__main__":
#     enqueueTaskToDisplayURL("http://example.com/")
#     reactor.run()
