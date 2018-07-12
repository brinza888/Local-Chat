from Message import Message
from Commands import *


class Executor:
    noPermission = Message.get_error("You haven't enough permissions!")
    wrongArg = Message.get_error("Invalid argument!")
    cmdNotFound = Message.get_error("Command not found!")
    userNotFound = Message.get_error("User  not found!")

    def __init__(self, server):
        self.server = server

    def execute(self, name, caller, args):
        if name not in globals().keys():
            caller.send(Executor.cmdNotFound)
            return

        cmd = globals()[name]

        if cmd.isadmin and not caller.admin:
            caller.send(Executor.noPermission)
            return

        if len(args) == 1:
            if args[0] == "help":
                caller.send(cmd.help_txt)
                return

        cmd.execute(caller, args, self)
