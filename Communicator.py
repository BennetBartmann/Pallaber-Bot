import Connection

__author__ = 'Pups'


class Communicator(object):
    def __init__(self):
        self.user = []
        self.last_activity = Connection.Connection.time()
        self.counter = None