from twisted.internet import defer, reactor

num = 0

def run_later(seconds, function, *args, **kwargs):
    d = defer.Deferred()

    def fire():
        value = function(*args, **kwargs)
        d.callback(value)

    reactor.callLater(seconds, fire)
    return d

def print_stuff(message):
    # Because 'print' is a *statement*.
    print (message)

def handleResult(result):
    global num; num += 1
    print ("callback %s" % (num,))
    print ("\tgot result: %s" % (result,))
    return "yay! handleResult was successful!"

d = run_later(2, print_stuff, 'Hello')
d.addCallback(lambda x: handleResult("elo"))
d.addCallback(lambda ignored: run_later(3, print_stuff, 'World'))

run_later(3, print_stuff, 'Beautiful')


# reactor.callLater(5, reactor.stop)
reactor.run()

