import re
import defaultlib
import urllib
from ModulePrototype import ModulePrototype
import Connection
class Title(ModulePrototype):
    def use(self, nick, action, where, what):
        if re.search("(?P<url>https?://[^\s]+)", what)is not None:
            try:
                content = urllib.urlopen(re.search("(?P<url>https?://[^\s]+)", what).group("url")).read()
                titleRE = re.compile("<title>(.+?)</title>")
                title = titleRE.search(content).group(1)
                defaultlib.defaultlib.send(title, Connection.channel)
            except:
                #defaultlib.defaultlib.send("URL nicht parsebar", Connection.channel)
