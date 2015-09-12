from ModulePrototype import ModulePrototype
import Connection

class UserList(ModulePrototype):

    def use(self, nick, action, where, what):
        if action == "JOIN":
            self.communicator.user.append(nick)
        if (action == "PART" or action == "QUIT") and nick in self.communicator.user:
            self.communicator.user.remove(nick)
        if action == "PRIVMSG" and nick not in self.communicator.user:
            self.communicator.user.append(nick)
        if action == "PRIVMSG" and what.find("PING") == -1:
            if (Connection.debug):
                print 'no ping?'
            self.communicator.last_activity = Connection.Connection.time()

