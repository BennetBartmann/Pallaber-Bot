import socket
from Communicator import Communicator
from Seen import Seen
from Title import Title
from UserList import UserList
from Counter import Counter
from defaultlib import defaultlib
import random
import math
import time
random.seed()

fobj_in = open("citations.txt")
citations = []
for cit in fobj_in:
    citations.append(cit.rstrip())

network = 'irc.freenode.org'
port = 6667
channel = "#autistenchat"
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )

irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
defaultlib(irc)
irc.send ( 'NICK LaberBot_Testversion\r\n' )
irc.send ( 'USER botty botty botty :IRC Bot\r\n' )
irc.send ( 'JOIN ' + channel + '\r\n' )
communicator = Communicator()
modules = []
modules.append(UserList(communicator))
modules.append(Counter(communicator))
modules.append(Seen(communicator))
modules.append(Title(communicator))
max_citation_interval = 3600
while True:
    data = irc.recv ( 4096 )

    if data.find ( 'PING' ) != -1:
        irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
        p = math.exp((time.time()-communicator.last_activity)/max_citation_interval) * 1000/math.exp(1)
        print(p)
        if random.randint(0,1000) < p:
            irc.send("PRIVMSG ' + channel + ' :"+random.choice(citations)+'\r\n')
    data = data.rstrip()
    try:
        where = ''.join (data.split(':')[:2]).split (' ')[-2]
        action = ''.join (data.split(':')[:2]).split (' ')[-3]
        user = data.split('!')[ 0 ].replace(':',' ')
        if action != "PRIVMSG":
             action = action = ''.join (data.split(':')[:2]).split (' ')[-2]
             where = ''.join (data.split(':')[:2]).split (' ')[-1]
    except:
        print "Unparsable Message"
    try:
        what = ':'.join(data.split (':')[2:])
    except:
        print "No Info"
    user = user.rstrip()
    user = user.lstrip()
    print data
    for module in modules:
        module.use(user,action,where,what)
