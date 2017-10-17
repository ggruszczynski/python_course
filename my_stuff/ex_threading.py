import threading
import time


class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=0.5):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=('elo',))
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self, msg):
        """ Method that runs forever """
        while True:
            # Do something
            print('Doing something imporant in the background:', msg)

            time.sleep(self.interval)

example = ThreadingExample()
time.sleep(3)
print('Checkpoint')
time.sleep(2)
print('Bye')



def MyThread1(msg):
    print('MyThread1 something imporant in the background:', msg)

def MyThread2(msg):
    print('MyThread1 something imporant in the background:', msg)


t1 = threading.Thread(target=MyThread1, args=('hoho',))
t2 = threading.Thread(target=MyThread2, args=['buuu'])
t1.start()
t2.start()