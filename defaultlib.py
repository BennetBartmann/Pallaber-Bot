import Connection
__author__ = 'Pups'
class defaultlib(object):
    def __init__(self, irc):
        defaultlib.irc = irc
    irc = None
    @staticmethod
    def send(what, where=Connection.channel):
        defaultlib.irc.send('PRIVMSG ' + where + ' :' + what
                            + '\r\n')

    @staticmethod
    def debug(message):
        if Connection.debug:
            print(message.encode())