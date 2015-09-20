from ModulePrototype import ModulePrototype
import pickle
import defaultlib
from collections import defaultdict
import Connection

__author__ = 'Pups'
class Seen(ModulePrototype):
    def __init__(self, communicator):
        ModulePrototype.__init__(self, communicator)
        self.user = defaultdict(int)
        try:
             with open("userseen.stats", "rb") as picklefile:
                self.user = pickle.load(picklefile)
        except:
            print ("No time pickle loadable")

    def use(self, nick, action, where, what):
        if action != "PRIVMSG":
            return
        self.user[nick] = Connection.Connection.time()
        with open("userseen.stats", "wb") as picklefile:
            pickle.dump(self.user, picklefile)
        if what.find(".seen") != -1:
            self._seen(nick, what)
        if what.find(".activ") != -1:
            self._activity(nick)
        if what.find(".mods") != -1:
            self._mods(nick)

    def _seen(self,nick,what):
        if not self.communicator.counter.user_authorized(nick, 25):
            defaultlib.send(nick + ": tut mir leid ich darf dir hierrauf noch nicht antworten", Connection.channel)
            return
        who = what.split(' ')[1]
        print (who)
        if self.user.get(who, None) is not None:
            defaultlib.send(nick + ":" + who + " sah ich zuletzt vor " + str(
                (Connection.Connection.time() - self.user[who]) / 60000) + " Minuten", Connection.channel)
        else:
            defaultlib.send(nick + ":" + who + " hab ich noch nicht gesehen, tut mir leid", Connection.channel)

    def _idle_old(self, nick):
        cnt = 0
        for name, activity in sorted(self.user.iteritems(), key = lambda k,v: (v,k), reverse=True):
            if self.user.get(name, None) is not None:
                if name not in self.communicator.user:
                    continue
                cnt += 1
                defaultlib.send(name + "<-" + str((Connection.Connection.time() - activity) / 60000) + " Minuten",
                                Connection.channel)
                if cnt > 2:
                    break


    def _activity(self, nick):
        cnt = [0,0,0] # zwanzig, sechs, zwei minuten
        for name, activity in sorted(self.user.iteritems(), key = lambda k,v: (v,k), reverse=True):
            if self.user.get(name, None) is not None:
                if name not in self.communicator.user:
                    continue
                idle = (Connection.Connection.time()-activity)/60000
                if idle <= 20:
                    cnt[0] += 1
                if idle <= 6:
                    cnt[1] += 1
                if idle <= 2:
                    cnt[2] += 1
        defaultlib.send('User in den letzten 20 Minuten: ' + str(cnt[0]) + ', 6 Minuten: '
                        + str(cnt[1]) + ', gerade eben: ' + str(cnt[2]))


    def _mods(self, nick):
        mods = []
        with open("mods.txt", "rb") as fobj_in:
            for mod in fobj_in:
                mods.append(mod.rstrip())
        current_mods = []
        outstring = "Aktuell sind folgende Moderatoren online: "
        for usr in self.communicator.user:
            if usr in mods:
                current_mods.append(usr)
                outstring += usr + " "
        if current_mods.__len__() != 0:
            defaultlib.send(outstring, nick)
        else:
            defaultlib.send("Leider scheint momentan kein Moderator online zu sein.", nick)


