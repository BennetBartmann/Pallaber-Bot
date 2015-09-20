import socket
import Connection
__author__ = 'Pups'

irc = None

def send(what, where=Connection.channel):
    irc.send('PRIVMSG '.encode() + where.encode() + ' :'.encode() +
             what.encode() + '\r\n'.encode())

def debug(message):
    if Connection.debug:
        print(message)

def init():
    test= 0
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    irc.connect((Connection.network, Connection.port))
    print(irc.recv(4096))
    irc.send('NICK '.encode() + Connection.nick.encode() + '\r\n'.encode())
    irc.send('USER botty botty botty :IRC Bot\r\n'.encode())
    irc.send('JOIN '.encode() + Connection.channel.encode() + '\r\n'.encode())

def recv():
    data = irc.recv(4096)
    if data.find('PING') != -1:
        irc.send('PONG '.encode() + data.split()[1].encode() + '\r\n'.encode())
    return data.rstrip()

