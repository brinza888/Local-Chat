from Messages.Error import Error
from Messages.Info import Info
from Commands import *


class Executor:
    SHOW_USAGE = "SHOW_USAGE"
    INVALID_ARG = "INVALID_ARG"

    def __init__(self, server):
        self.server = server

    def execute(self, name, caller, args):
        if name not in globals().keys():
            caller.send(Error("Command not found!"))
            return

        cmd = globals()[name]

        if cmd.isadmin and not caller.admin:
            caller.send(Error("You haven't enough permissions!"))
            return

        if len(args) == 1:
            if args[0] == "help":
                caller.send(Info(cmd.help_txt))
                return

        code = cmd.execute(caller, args, self)

        if code is Executor.INVALID_ARG:
            caller.send(Error("Invalid argument!"))
        elif code is Executor.SHOW_USAGE:
            caller.send(Error("Syntax: ") + cmd.syntax)
