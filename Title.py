import re
import defaultlib
import urllib
from ModulePrototype import ModulePrototype
import Connection
class Title(ModulePrototype):
    def use(self, nick, action, where, what):
        url = re.search("(?P<url>https?://[^\s]+)", what)
        if url is not None:
            with open("links.txt", "ab") as links:
                links.write(what + "\n")
            try:
                content = urllib.urlopen(url.group("url")).read()
                titleRE = re.compile("<title>(.+?)</title>")
                title = titleRE.search(content).group(1)
                defaultlib.send(title, Connection.channel)
            except:
                if what == 'http://www.rehakids.de/phpBB2/ftopic112457.html':
                    defaultlib.send('PDF Adressen zur Autismusdiagnostik :: REHAkids Das Forum für besondere Kinder :: Das Forum für behinderte Kinder.')
                    return
                defaultlib.debug("URL nicht parsebar: " + what)