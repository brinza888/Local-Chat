help_txt = "Give admin power to user"
isadmin = True


def execute(caller, args, ex):
    if len(args) < 1:
        caller.send(ex.wrongArg)
        return
    user = ex.server.nick2user(args[0])
    if not user:
        caller.send(ex.userNotFound)
        return
    user.admin = True
