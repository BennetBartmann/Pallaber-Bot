__author__ = 'Daniela'
from ModulePrototype import ModulePrototype
import Connection
import defaultlib
import wikipedia

class Query(ModulePrototype):

    def use(self, nick, action, where, what):
        if action != "PRIVMSG":
            return
        if what.find(".g") != -1:
            self._google(nick, what)
        if what.find(".w") != -1:
            self._wiki(nick, what)

    def _google(self, nick, what):
        test = 0
        # jo, hier wird gegoogelt

    def _wiki(self, nick, what):
        test = 0
        # jo, hier wird wikipedia durchsucht
        


