import pickle
import threading
import socket
from Messages.Info import Info
from Messages.Bcast import Bcast
from Messages.Error import Error


class User:
    count = 0
    notOnServer = Error("User not on server!")

    def __init__(self, ip, conn, server):
        self.admin = False
        self.ip = ip
        self.__conn = conn
        self.nick = "Guest#" + str(User.count)
        self.server = server
        self.__th = threading.Thread(target=self.receive, daemon=True)
        self.__onServer = False

    def accept_success(self):
        if self.__onServer:
            return
        self.join_leave_msg("Connected")
        self.send(Info("Connect success! Welcome on IP: ") + self.server.HOST)
        self.server.users.append(self)
        User.count += 1
        self.__onServer = True
        self.__th.start()

    def accept_canceled(self, reason):
        if not self.__onServer:
            return
        self.send(Info("Connect canceled, because: ") + reason)
        self.disconnect()

    def join_leave_msg(self, text):
        msg = "{0} {1} ({2})".format(text, self.nick, self.ip)
        self.server.resend(Bcast(msg))

    def receive(self):
        while self.__onServer:
            try:
                data = self.__conn.recv(1024)
            except socket.error:
                self.disconnect()
                return
            except ConnectionResetError:
                self.disconnect()
                return
            if not data:
                continue
            message = pickle.loads(data)
            message.owner = self.nick
            self.server.manager(message, self)

    def send(self, msg):
        data = pickle.dumps(msg)
        try:
            self.__conn.send(data)
        except ConnectionResetError:
            if self.__onServer:
                self.disconnect()
                return User.notOnServer

    def disconnect(self, reason="You disconnected!"):
        if not self.__onServer:
            return User.notOnServer
        if self in self.server.users:
            self.server.users.remove(self)
        self.__onServer = False
        self.send(Info("You disconnected, because: ") + reason)
        self.__conn.close()
        self.join_leave_msg("Disconnected")
