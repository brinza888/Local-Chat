from datetime import datetime


class Message (object):
    def __init__(self, text):
        self.owner = "*???*"
        self.text = text

    def __add__(self, other):
        if isinstance(other, Message):
            other = other.text
        self.text += other
        return self

    def get_text(self):
        dt = datetime.strftime(datetime.now(), "[%d.%m %H:%M]")
        return "{0} {1}: {2}".format(dt, self.owner, self.text)
