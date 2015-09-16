__author__ = 'Daniela'
from ModulePrototype import ModulePrototype
import Connection
from defaultlib import defaultlib
import wikipedia

class Query(ModulePrototype):

    def use(self, nick, action, where, what):
        if action != "PRIVMSG":
            return
        if what.find(".g ") != -1:
            self._google(nick, what)
        if what.find(".w ") != -1:
            self._wiki(nick, what)

    def _google(self, nick, what):
        test = 0
        # jo, hier wird gegoogelt

    def _wiki(self, nick, what):
        # jo, hier wird wikipedia durchsucht
        if not self.communicator.counter.user_authorized(nick):
            defaultlib.send("Wikipedia soll ich durchsuchen? Schau doch lieber in ein richtiges Lexikon!", Connection.channel)
            return
        w = wikipedia.set_lang('de')
        q = what.split(' ')
        query = ''
        for word in q:
            if word != '.w':
                query += word + ' '
        w = wikipedia.search(query)
        if w.__len__() == 0:
            defaultlib.send(nick +
                            ', in Wikipedia finde ich dazu nichts. Möchtest du einen Artikel darüber schreiben?',
                            Connection.channel)
            return
        page = wikipedia.WikipediaPage(w.pop(0))
        defaultlib.send(nick + ' ' + page.url, Connection.channel)
        defaultlib.send(page.summary, Connection.channel)


