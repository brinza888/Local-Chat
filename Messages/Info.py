from Messages.Message import Message


class Info (Message):
    def get_text(self):
        return "INFO: " + self.text
