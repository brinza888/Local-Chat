help_txt = "Add user ip at server blacklist"
isadmin = True


def execute(caller, args, ex):
    if len(args) < 1:
        caller.send(ex.wrongArg)
        return

    user = ex.server.nick2user(args[0])
    if not user:
        caller.send(ex.userNotFound())
    ex.server.ban(user.ip)
