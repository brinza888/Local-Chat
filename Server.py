import socket
import threading
from User import User
from Executor import Executor
from Messages import *


class Server:
    youBanned = Info.Info("Your ip have been banned!")
    userNotFound = Error.Error("User not found!")
    alreadyBanned = Error.Error("This ip already banned!")
    notBanned = Error.Error("This ip has not banned!")

    def __init__(self, ip, port=9090, max_users=10):
        self.console = False
        self.HOST = ip
        self.PORT = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.HOST, self.PORT))
        self.sock.listen(max_users)
        self.blacklist = []
        self.users = []
        self.ex = Executor(self)
        self.th = threading.Thread(target=self.acceptor)
        self.th.start()

    def set_console(self, ip):
        self.console = ip

    def manager(self, msg, owner):
        print(msg.get_text())
        if msg.text[0] == "/":
            name = msg.text[1:].split()[0]
            args = msg.text[1:].split()[1:]
            self.ex.execute(name, owner, args)
        else:
            self.resend(msg)

    def resend(self, msg):
        if isinstance(msg, Bcast.Bcast):
            print(msg.get_text())
        for u in self.users:
            u.send(msg)

    def acceptor(self):
        while True:
            conn, addr = self.sock.accept()
            u = User(addr[0], conn, self)
            if u.ip not in self.blacklist:
                u.accept_success()
                if u.ip == self.console:
                    u.admin = True
                    self.console = ""
            else:
                u.accept_canceled(Server.youBanned)

    def nick2user(self, nick):
        for u in self.users:
            if u.nick == nick:
                return u
        return Server.userNotFound

    def ban(self, ip):
        if ip in self.blacklist:
            return Server.alreadyBanned
        self.blacklist.append(ip)

    def unban(self, ip):
        if ip not in self.blacklist:
            return Server.notBanned
        self.blacklist.remove(ip)


if __name__ == "__main__":
    print("Local-Chat v0.2.1 Server")
    HOST = input("Bind ip: ")
    server = Server(HOST)
    server.set_console(HOST)
