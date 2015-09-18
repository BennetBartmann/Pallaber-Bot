import socket
from Communicator import Communicator
from Seen import Seen
from Title import Title
from UserList import UserList
from Counter import Counter
from defaultlib import defaultlib
from Query import Query
from Citations import Citations
import Connection
import traceback

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

irc.connect((Connection.network, Connection.port))
print(irc.recv(4096))
defaultlib(irc)
irc.send(bytes('NICK ' + Connection.nick + '\r\n', encoding='utf8'))
irc.send(bytes('USER botty botty botty :IRC Bot\r\n', encoding='utf8'))
irc.send(bytes('JOIN ' + Connection.channel + '\r\n', encoding='utf8'))
communicator = Communicator()

modules = []
count = Counter(communicator)
cite = Citations(communicator)
communicator.counter = count

modules.append(UserList(communicator))
modules.append(count)
modules.append(Seen(communicator))
modules.append(Title(communicator))
modules.append(Query(communicator))
modules.append(cite)

while True:
    data = irc.recv(4096)

    cite._cite()

    if data.find('PING'.encode()) != -1:
        irc.send('PONG '.encode() + data.split()[1] + '\r\n'.encode())

    data = data.rstrip()
    error_free = True
    try:
        where = ''.join(data.split(':')[:2]).split(' ')[-2]
        action = ''.join(data.split(':')[:2]).split(' ')[-3]
        user = data.split('!')[0].replace(':', ' ')
        if action != "PRIVMSG":
            action = action = ''.join(data.split(':')[:2]).split(' ')[-2]
            where = ''.join(data.split(':')[:2]).split(' ')[-1]
    except:
        print("Unparsable Message")
        error_free = False
        print(data)

    try:
        what = ':'.join(data.split(':')[2:])
    except:
        print ("No Info")
    #print data
    if error_free:
        user = user.rstrip()
        user = user.lstrip()
        for module in modules:
            try:
                module.use(user, action, where, what)
            except Exception as error:
                #print "Error in Module"
                #print user + ': ' + what
                import traceback
                #print traceback.format_exc()
