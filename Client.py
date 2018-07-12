from tkinter import *
import socket
import threading
import pickle
from Message import Message

sock = False
wrongAddr = Message.get_error("Wrong ip address")
failedServer = Message.get_error("Failed to find server")


def setup(ip):
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((ip, 9090))
    except socket.gaierror:
        show_msg(wrongAddr)
        sock = False
        return
    except OSError:
        show_msg(failedServer)
        sock = False
        return
    th = threading.Thread(target=receive)
    th.daemon = True
    th.start()


root = Tk()
root.title("ChatClient v0.1")
root.geometry("500x400")
root.resizable(False, False)

chatForm = Text(root, height=19, width=54, font="Arial 12", wrap=WORD)
chatForm.place(x=250, y=185, anchor="center")


def send(ev):
    global sock, entry
    txt = entry.get()
    entry.delete("0", END)
    if not sock:
        setup(txt)
        return
    if len(txt) == 0:
        return
    message = Message(txt)
    data = pickle.dumps(message)
    sock.send(data)


entry = Entry(root, width=46, font="Arial 12")
entry.place(x=214, y=378, anchor="center")
entry.bind("<Return>", send)

btSend = Button(root, text="Send", width=5, height=1, font="Arial 12")
btSend.place(x=460, y=378, anchor="center")
btSend.bind("<Button-1>", send, "+")


def show_msg(msg):
    txt = msg.get() + "\n"
    chatForm.insert(END, txt)


def receive():
    global sock
    while True:
        try:
            data = sock.recv(1024)
        except socket.error:
            return
        if not data:
            continue
        message = pickle.loads(data)
        show_msg(message)


root.mainloop()
