import socket
from Communicator import Communicator
from Seen import Seen
from Title import Title
from UserList import UserList
from Counter import Counter
import defaultlib
from Query import Query
from Citations import Citations
import Connection
import traceback

defaultlib.init()
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
    data = defaultlib.recv()

    cite._cite()

    error_free = True
    try:
        where = data.split(':')[1].split(' ')[2]
        action = data.split(':')[1].split(' ')[1]
        user = data.split('!')[0].replace(':', ' ')
        if action != "PRIVMSG".encode():
            action = data.split(':')[1].split(' ')[1]
            where = data.split(':')[1].split(' ')[2]
    except:
        print("Unparsable Message")
        error_free = False
        print(data)

    try:
        what = data.split(':')[2]
    except:
        print ("No Info")
    #print data
    if error_free:
        user = user.rstrip()
        user = user.lstrip()
        user = user.casefold()
        for module in modules:
            try:
                module.use(user, action, where, what)
            except Exception as error:
                #print "Error in Module"
                #print user + ': ' + what
                import traceback
                #print traceback.format_exc()
