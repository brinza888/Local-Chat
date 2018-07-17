from Messages.Info import Info

help_txt = "Shows user IP"
isadmin = False
syntax = "/whois [nick]"


def execute(caller, args, ex):
    if len(args) < 1:
        return ex.SHOW_USAGE

    res = ex.server.nick2user(args[0])
    if res is ex.server.userNotFound:
        return ex.server.INVALID_ARG

    caller.send(Info("User IP: " + res.ip))
