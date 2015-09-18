from ModulePrototype import ModulePrototype
import pickle
import defaultlib
import Connection
__author__ = 'Pups'
from collections import defaultdict
class Counter(ModulePrototype):
    def __init__(self, communicator):
        ModulePrototype.__init__(self, communicator)
        self.user = defaultdict(int)
        try:
            with open("userstats.stats", "rb") as picklefile:
                self.user = pickle.load(picklefile)
        except:
            print ("No pickle loadable")

    def use(self, nick, action, where, what):
        print [nick, action, where, what]
        if nick == Connection.nick:
            return
        if where != Connection.channel:
            return

        if action == "PRIVMSG":
            self.user[nick] += len(what)
        if action == "JOIN" and self.user[nick] == 0:
            if len(self.communicator.user) > 2:
                defaultlib.defaultlib.send(
                    "Hallo " + nick + ", willkommen im Chat! Ich bin der Bot dieses Channels. Du koenntest hallo sagen, die anderen Anwesenden antworten sicher auch bald.",                    where)
            else:
                defaultlib.defaultlib.send(
                    "Hallo " + nick + ", willkommen im Chat! Ich bin der Bot dieses Channels. Du hast gerade eine schlechte Zeit erwischt, meist ist hier in den Morgen und Abendstunden mehr los!",
                    where)
        with open("userstats.stats", "wb") as picklefile:
            pickle.dump(self.user, picklefile)
        #if what.find(".stats") != -1:
        #    self._print_stats()

    def _print_stats(self):
        print ("here")
        out_str = ""
        for user, number in sorted(self.user.iteritems(), key = lambda k,v: (v,k), reverse=True):
            out_str += user+":"+str(number)+";"
            if len(out_str) > 150:
                defaultlib.defaultlib.send(out_str)
                out_str = ""
        defaultlib.defaultlib.send(out_str)

    def user_authorized(self, quser, percent = 5):
        counts = 0
        users = 0
        for usr in self.user.itervalues():
            counts += usr
            users += 1
        average = counts/users
        #print average
        allowance =  average * (percent / 100.0)
        #print allowance
        if self.user[quser] > allowance:
            return True
        else:
            return False



