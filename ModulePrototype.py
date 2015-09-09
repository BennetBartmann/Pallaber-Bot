__author__ = 'Pups'
class ModulePrototype(object):
    def __init__(self, communicator):
        self.communicator = communicator
    def use(self, nick, action, where, what):
        return ""