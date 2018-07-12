from Message import *

help_txt = "Change your nick"
isadmin = False


def execute(caller, args, ex):
    if len(args) < 1:
        caller.send(ex.wrongArg)
        return

    old = caller.nick
    caller.nick = args[0]
    ex.server.resend(Message.get_info(old + " -> " + args[0]))
