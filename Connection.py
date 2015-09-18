__author__ = 'Daniela'
channel = '#pallaber-bot'.encode()
network = 'irc.freenode.org'.encode()
port = 6667
nick = 'LaberBot_Testversion'.encode()
debug = True

import time

class Connection:
    @staticmethod
    def time():
        return int(round(time.time() * 1000))
