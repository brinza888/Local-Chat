import socket
import threading
import sys
from User import User
from Executor import Executor
from Message import Message


class Server:
    ipBanned = Message.get_bcast("Banned ip: ")
    ipUnBanned = Message.get_bcast("Unbanned ip: ")
    userBanned = Message.get_bcast("Banned user: ")
    youBanned = Message.get_info("Your ip have been banned!")
    userNotFound = Message.get_error("User  not found!")

    def __init__(self, ip, port=9090):
        self.console = False
        self.HOST = ip
        self.PORT = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.HOST, self.PORT))
        self.sock.listen(5)
        self.blacklist = []
        self.users = []
        self.th = threading.Thread(target=self.acceptor)
        self.th.start()
        self.ex = Executor(self)
        self.welcomeMsg = Message.get_info("Welcome on server: " + self.HOST)

    def set_console(self, ip):
        self.console = ip

    def manager(self, msg, owner):
        if msg.text[0] == "/":
            name = msg.text[1:].split()[0]
            args = msg.text[1:].split()[1:]
            self.ex.execute(name, owner, args)
        else:
            self.resend(msg)

    def resend(self, msg):
        for u in self.users:
            u.send(msg)

    def acceptor(self):
        while True:
            conn, addr = self.sock.accept()
            u = User(addr[0], conn, self)
            if u.ip not in self.blacklist:
                self.users.append(u)
                print("New user", addr[0])
                u.send(self.welcomeMsg)
                if u.ip == self.console:
                    u.admin = True
                    self.console = ""
            else:
                u.send(Server.youBanned)

    def nick2user(self, nick):
        for u in self.users:
            if u.nick == nick:
                return u
        return False

    def ban(self, ip):
        self.blacklist.append(ip)
        for u in self.users:
            if u.ip == ip:
                self.resend(Server.userBanned + u.nick)
                u.disconnect()
                return
        self.resend(Server.ipBanned + ip)

    def unban(self, ip):
        self.blacklist.remove(ip)
        self.resend(Server.ipUnBanned + ip)


HOST = input("Bind ip: ")
server = Server(HOST)
server.set_console("127.0.0.1")
