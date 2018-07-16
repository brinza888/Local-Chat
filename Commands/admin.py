help_txt = "Give admin power to user"
isadmin = True
syntax = "/admin [nick]"


def execute(caller, args, ex):
    if len(args) < 1:
        return ex.SHOW_USAGE

    user = ex.server.nick2user(args[0])
    if user is ex.server.userNotFound:
        return ex.INVALID_ARG
    user.admin = True
