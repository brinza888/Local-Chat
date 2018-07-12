from datetime import datetime


class Message:
    ERROR = "ERROR"
    BCAST = "BCAST"
    INFO = "INFO"
    WARN = "WARN"
    DEFAULT = ""

    @staticmethod
    def get_info(text):
        return Message(text, Message.INFO)

    @staticmethod
    def get_bcast(text):
        return Message(text, Message.BCAST)

    @staticmethod
    def get_error(text):
        return Message(text, Message.ERROR)

    @staticmethod
    def get_warn(text):
        return Message(text, Message.WARN)

    def __init__(self, text, msg_type=DEFAULT):
        self.owner = "*?*"
        self.text = text
        self.msg_type = msg_type

    def __add__(self, other):
        self.text += other

    def get(self):
        txt = ""
        if self.msg_type == Message.DEFAULT:
            txt += datetime.strftime(datetime.now(), "[%d.%m %H:%M]")
            txt += "[" + self.owner + "]: " + self.text
        else:
            txt += self.msg_type + ": " + self.text
        return txt
