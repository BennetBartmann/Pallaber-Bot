import socket
from Communicator import Communicator
from Seen import Seen
from Title import Title
from UserList import UserList
from Counter import Counter
from defaultlib import defaultlib
from Query import Query
import random
import math
import Connection
random.seed()

import sys
reload(sys)
sys.setdefaultencoding('utf8')



fobj_in = open("citations.txt")
citations = []
for cit in fobj_in:
    citations.append(cit.rstrip())

irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )

irc.connect ( ( Connection.network, Connection.port ) )
print irc.recv ( 4096 )
defaultlib(irc)
irc.send ( 'NICK '+Connection.nick+'\r\n' )
irc.send ( 'USER botty botty botty :IRC Bot\r\n' )
irc.send ( 'JOIN ' + Connection.channel + '\r\n' )
communicator = Communicator()
modules = []
modules.append(UserList(communicator))
modules.append(Counter(communicator))
modules.append(Seen(communicator))
modules.append(Title(communicator))
modules.append(Query(communicator))
max_citation_interval = 3600000
min_citation_interval = 600000
while True:
    data = irc.recv ( 4096 )

    if data.find ( 'PING' ) != -1:
        irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
        if ((Connection.Connection.time()-communicator.last_activity)/min_citation_interval > 0):
            p = math.log((Connection.Connection.time()-communicator.last_activity)/min_citation_interval)
        else:
            p = 0
        if (Connection.debug):
            print(p)
        if random.random() < p:
            irc.send('PRIVMSG ' + Connection.channel + ' :'+random.choice(citations).encode('utf-8') + '\r\n')
            if (Connection.debug):
                print(str((Connection.Connection.time()-communicator.last_activity) / 60000) +
                      'Minuten seit letzter Aktivity beim Random-Spruch-aufsagen')
            communicator.last_activity = Connection.Connection.time()
    data = data.rstrip()
    error_free = True
    try:
        where = ''.join (data.split(':')[:2]).split (' ')[-2]
        action = ''.join (data.split(':')[:2]).split (' ')[-3]
        user = data.split('!')[ 0 ].replace(':',' ')
        if action != "PRIVMSG":
             action = action = ''.join (data.split(':')[:2]).split (' ')[-2]
             where = ''.join (data.split(':')[:2]).split (' ')[-1]
    except:
        print "Unparsable Message"
        error_free = False

    try:
        what = ':'.join(data.split (':')[2:])
    except:
        print "No Info"
    user = user.rstrip()
    user = user.lstrip()
    print data
    if error_free:
        for module in modules:
            module.use(user,action,where,what)
