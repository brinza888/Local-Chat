help_txt = "Add ip at server blacklist"
isadmin = True


def execute(caller, args, ex):
    if len(args) < 1:
        caller.send(ex.wrongArg)
        return

    ex.server.ban(args[0])
