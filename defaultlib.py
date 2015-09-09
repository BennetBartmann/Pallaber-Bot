__author__ = 'Pups'
class defaultlib(object):
    def __init__(self, irc):
        defaultlib.irc = irc
    irc = None
    @staticmethod
    def send(where, what):
        defaultlib.irc.send('PRIVMSG ' + where + ' :' + what + '\r\n')