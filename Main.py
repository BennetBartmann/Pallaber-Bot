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
irc.send('NICK '.encode() + Connection.nick + '\r\n'.encode())
irc.send('USER botty botty botty :IRC Bot\r\n'.encode())
irc.send('JOIN '.encode() + Connection.channel + '\r\n'.encode())
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
        where = data.split(':'.encode())[1].split(' '.encode())[2]
        action = data.split(':'.encode())[1].split(' '.encode())[1]
        user = data.split('!'.encode())[0].replace(':'.encode(), ' '.encode())
        if action != "PRIVMSG".encode():
            action = data.split(':'.encode())[1].split(' '.encode())[1]
            where = data.split(':'.encode())[1].split(' '.encode())[2]
    except:
        print("Unparsable Message")
        error_free = False
        print(data)

    try:
        what = data.split(':'.encode())[2]
    except:
        print ("No Info")
    #print data
    if error_free:
        user = user.rstrip()
        user = user.lstrip()
        user = user.decode().casefold().encode()
        for module in modules:
            try:
                module.use(user, action, where, what)
            except Exception as error:
                #print "Error in Module"
                #print user + ': ' + what
                import traceback
                #print traceback.format_exc()
