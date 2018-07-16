from Messages.Bcast import Bcast

help_txt = "Remove user ip from server blacklist"
isadmin = True
syntax = "/unban [ip]"


def execute(caller, args, ex):
    if len(args) < 1:
        return ex.SHOW_USAGE

    ip = args[0]
    res = ex.server.unban(ip)
    if res is ex.server.notBanned:
        caller.send(ex.server.notBanned)
        return
    ex.server.resend(Bcast("IP unbanned: ") + ip)
