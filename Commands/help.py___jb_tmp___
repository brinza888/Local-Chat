from Commands import __all__
from Messages.Info import Info

help_txt = "Shows all available commands"
isadmin = False
syntax = "/help"


def execute(caller, args, ex):
    caller.send(Info("Available commands: " + ", ".join(__all__)))
