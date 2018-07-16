from Messages.Message import Message


class Bcast (Message):
    def get_text(self):
        return "BCAST: " + self.text
