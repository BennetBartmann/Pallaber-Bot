import socket
import Connection
__author__ = 'Pups'

irc = None

def send(what, where=Connection.channel):
    global irc
    irc.send('PRIVMSG '.encode() + where.encode() + ' :'.encode() +
             what.encode() + '\r\n'.encode())

def debug(message):
    if Connection.debug:
        print(message)

def init():
    global irc
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    irc.connect((Connection.network, Connection.port))
    print(irc.recv(4096))
    irc.send('NICK '.encode() + Connection.nick.encode() + '\r\n'.encode())
    irc.send('USER botty botty botty :IRC Bot\r\n'.encode())
    irc.send('JOIN '.encode() + Connection.channel.encode() + '\r\n'.encode())

def recv():
    global irc
    data = irc.recv(4096)
    if data.find('PING'.encode()) != -1:
        irc.send('PONG '.encode() + data.split()[1] + '\r\n'.encode())
    data = data.rstrip()
    return data.decode(encoding='UTF-8')

