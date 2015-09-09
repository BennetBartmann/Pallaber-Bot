__author__ = 'Pups'
import time
class Communicator(object):
    def __init__(self):
        self.user = []
        self.last_activity = int(round(time.time() * 1000))