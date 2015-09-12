from ModulePrototype import ModulePrototype
import time
import pickle
from defaultlib import defaultlib
from collections import defaultdict
import Connection

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
        if action != "PRIVMSG":
            return
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
            defaultlib.send(Connection.channel, nick + ":" + who + " sah ich zuletzt vor "+ str((self._current_milli_time()-self.user[who])/60000)+ " Minuten")
        else:
            defaultlib.send(Connection.channel, nick + ":" + who +" hab ich noch nicht gesehen, tut mir leid")

    def _idle(self, nick):
        cnt = 0
        for name, activity in sorted(self.user.iteritems(), key = lambda (k,v): (v,k), reverse=True):
            if self.user.get(name, None) is not None:
                if name not in self.communicator.user:
                    continue
                cnt += 1
                defaultlib.send(Connection.channel,name +"<-"+str((self._current_milli_time()-activity)/60000)+" Minuten")
                if cnt > 2:
                    break
    _current_milli_time = lambda self: int(round(time.time() * 1000))
