from Messages.Info import Info

help_txt = "Show online users"
isadmin = False
syntax = "/list"


def execute(caller, args, ex):
    nicks = []
    for u in ex.server.users:
        nicks.append(u.nick)
    caller.send(Info("Online users-> ") + ", ".join(nicks))
    nicks.clear()
