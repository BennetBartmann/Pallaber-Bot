import re
import defaultlib
import urllib
from ModulePrototype import ModulePrototype
import Connection
class Title(ModulePrototype):
    def use(self, nick, action, where, what):
        url = re.search("(?P<url>https?://[^\s]+)", what)
        if url is not None:
            try:
                content = urllib.urlopen(url.group("url")).read()
                titleRE = re.compile("<title>(.+?)</title>")
                title = titleRE.search(content).group(1)
                defaultlib.defaultlib.send(title, Connection.channel)
            except:
                if what == 'http://www.rehakids.de/phpBB2/ftopic112457.html':
                    defaultlib.defaultlib.send('PDF Adressen zur Autismusdiagnostik :: REHAkids Das Forum fuer besondere Kinder :: Das Forum fuer behinderte Kinder.')
                    return
                if Connection.debug:
                    print("URL nicht parsebar: " + what)

