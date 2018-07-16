from Messages.Bcast import Bcast
from Messages.Error import Error

help_txt = "Change your nick"
syntax = "/setnick [nick]"
isadmin = False


def execute(caller, args, ex):
    if len(args) < 1:
        return ex.SHOW_USAGE
    if args[0].lower().count("guest") >= 1:
        caller.send(Error("Nicks same to 'Guest#...' registered by system!"))
        return
    if ex.server.nick2user(args[0]) != ex.server.userNotFound:
        caller.send(Error("Nick already registered!"))
        return

    old = caller.nick
    caller.nick = args[0]
    ex.server.resend(Bcast(old + " -> " + args[0]))
