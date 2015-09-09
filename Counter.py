from ModulePrototype import ModulePrototype
import pickle
import defaultlib
__author__ = 'Pups'
from collections import defaultdict
class Counter(ModulePrototype):
    def __init__(self, communicator):
        ModulePrototype.__init__(self, communicator)
        self.user = defaultdict(int)
        try:
            picklefile = open("userstats.stats", "rb")
            self.user = pickle.load(picklefile)
            picklefile.close()
        except:
            print "No pickle loadable"

    def use(self, nick, action, where, what):
        print [nick, action, where, what]
        if nick == 'LaberBot':
            return
        if where != "#autistenchat":
            return

        if action == "PRIVMSG":
            self.user[nick] += len(what)
        print self.user[nick]
        if action == "JOIN" and self.user[nick] == 0:
            if len(self.communicator.user) > 2:
                defaultlib.defaultlib.send(where, "Hallo "+nick+" Willkommen im Chat, ich bin hier nur ein Diener, du koenntest dich vorstellen, die anderen Antworten sicher auch bald")
            else:
                defaultlib.defaultlib.send(where, "Hallo "+nick+" Willkommen im Chat, ich bin hier nur ein Diener, du hast eine schlechte Zeit erwischt meist ist hier in den Morgen und Abendstunden mehr los!")
        picklefile = open("userstats.stats", "wb")
        pickle.dump(self.user, picklefile)
        picklefile.close()
        if what.find(".stats") != -1:
            self._print_stats()

    def _print_stats(self):
        out_str = ""
        for user, number in sorted(self.user.iteritems(), key = lambda (k,v): (v,k), reverse=True):
            out_str += user+":"+str(number)+";"
            if len(out_str) > 150:
                defaultlib.defaultlib.send("#autistenchat", out_str)
                out_str = ""
        defaultlib.defaultlib.send("#autistenchat", out_str)



