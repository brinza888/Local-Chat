help_txt = "Remove user ip from server blacklist"
isadmin = True


def execute(caller, args, ex):
    if len(args) < 1:
        caller.send(ex.wrongArg)
        return

    ex.server.unban(args[0])
