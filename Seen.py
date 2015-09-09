from ModulePrototype import ModulePrototype
import time
import pickle
from defaultlib import defaultlib
from collections import defaultdict

__author__ = 'Pups'
class Seen(ModulePrototype):
    def __init__(self, communicator):
        ModulePrototype.__init__(self, communicator)
        self.user = defaultdict(int)
        try:
            picklefile = open("userseen.stats", "rb")
            self.user = pickle.load(picklefile)
            picklefile.close()
        except:
            print "No time pickle loadable"

    def use(self, nick, action, where, what):
        self.user[nick] = self._current_milli_time()
        picklefile = open("userseen.stats", "wb")
        pickle.dump(self.user, picklefile)
        picklefile.close()
        if what.find(".seen") != -1:
            self._seen(nick, what)
        if what.find(".idle") != -1:
            self._idle(nick)

    def _seen(self,nick,what):
        who = what.split(' ')[1]
        print (who)
        if self.user.get(who, None) is not None:
            defaultlib.send("#autistenchat", nick + ":" + who + " sah ich zuletzt vor "+ str((self._current_milli_time()-self.user[who])/60000)+ " Minuten")
        else:
            defaultlib.send("#autistenchat", nick + ":" + who +" hab ich noch nicht gesehen, tut mir leid")

    def _idle(self, nick):
        for usr in self.communicator.user:
            if self.user.get(usr, None) is not None:
               defaultlib.send("#autistenchat",usr +"<-"+str((self._current_milli_time()-self.user[usr])/60000)+" Minuten")
    _current_milli_time = lambda self: int(round(time.time() * 1000))