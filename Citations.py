from defaultlib import defaultlib

__author__ = 'Daniela'
from ModulePrototype import ModulePrototype
import Connection
import math
import random


class Citations(ModulePrototype):
    citations = []
    max_citation_interval = 3600000
    min_citation_interval = 600000


    def __init__(self, communicator):
        ModulePrototype.__init__(self,communicator)
        with open("citations.txt") as fobj_in:
            fobj_in = open("citations.txt")
            for cit in fobj_in:
                self.citations.append(cit.rstrip())
        random.seed()

    def use(self, nick, action, where, what):
        if action != "PRIVMSG".encode():
            return
        if what.find(".stfu".encode()) != -1:
            self._stfu()
        if what.find(".freq".encode()) != -1:
            self._freq()
        if what.find(".reset".encode()) != -1:
            self._reset()

    def _stfu(self):
        self.min_citation_interval *= 10

    def _freq(self):
        return

    def _reset(self):
        self.min_citation_interval = 600000

    def _cite(self):
        return
        p = (Connection.Connection.time()-self.communicator.last_activity)/self.min_citation_interval
        if (p > 0):
            p = math.log(p)
        else:
            p = 0
        if (Connection.debug):
            print(p)
        if len(self.communicator.user) > 0:
           p = (Connection.Connection.time()-self.communicator.last_activity)/self.min_citation_interval
           if (p > 0):
               p = math.log(p)
           else:
               p = 0
           if (Connection.debug):
               print(p)
           if random.random() < p:
                defaultlib.send(random.choice(self.citations) + '\r\n')
                defaultlib.debug(str((Connection.Connection.time()-self.communicator.last_activity) / 60000) +
                          'Minuten seit letzter Aktivity beim Random-Spruch-aufsagen')
                self.communicator.last_activity = Connection.Connection.time()

