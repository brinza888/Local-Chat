from Message import *

help_txt = "Show online users"
isadmin = False


def execute(caller, args, ex):
    nicks = []
    for u in ex.server.users:
        nicks.append(u.nick)
    caller.send(Message(", ".join(nicks), Message.INFO))
