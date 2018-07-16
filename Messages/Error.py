from Messages.Message import Message


class Error (Message):
    def get_text(self):
        return "ERROR: " + self.text
