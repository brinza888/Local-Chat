from Messages.Bcast import Bcast

help_txt = "Add user ip at server blacklist"
isadmin = True
syntax = "/ban [ip]"


def execute(caller, args, ex):
    if len(args) < 1:
        return ex.SHOW_USAGE

    ip = args[0]
    flag = False

    res = ex.server.ban(ip)
    if res is ex.server.alreadyBanned:
        caller.send(ex.server.alreadyBanned)
        return

    for u in ex.server.users:
        if u.ip == ip and not u.admin:
            u.disconnect(ex.server.youBanned)
            ex.server.resend(Bcast("User banned: {0} ({1})".format(u.nick, u.ip)))
            flag = True
    if not flag:
        ex.server.resend(Bcast("IP banned: ") + ip)
