__author__ = 'Daniela'
channel = '#pallaber-Bot'
network = 'irc.freenode.org'
port = 6667
nick = 'LaberBot_Testversion'
debug = True

import time

class Connection:
    @staticmethod
    def time():
        return int(round(time.time() * 1000))
