import pickle
import threading
import socket
from Message import Message


class User:
    count = 0

    def __init__(self, ip, conn, server):
        self.admin = False
        self.id = User.count
        self.ip = ip
        self.conn = conn
        self.nick = "Guest#" + str(self.id)
        self.server = server
        User.count += 1
        self.th = threading.Thread(target=self.receive)
        self.th.daemon = True
        self.th.start()

    def receive(self):
        while self.conn:
            try:
                data = self.conn.recv(1024)
            except socket.error:
                self.disconnect()
                return
            if not data:
                continue
            message = pickle.loads(data)
            message.owner = self.nick
            print(message.get())
            self.server.manager(message, self)

    def send(self, msg):
        data = pickle.dumps(msg)
        self.conn.send(data)

    def disconnect(self):
        self.server.users.remove(self)
        self.conn.close()
        txt = "Disconnected: " + self.nick + " (" + self.ip + ")"
        self.server.resend(Message.get_info(txt))
        print(txt)
