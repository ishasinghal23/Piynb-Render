class InvalidURLException(Exception):
    def __init__(self, message: str="URL is not valid"):
        self.messgae = message
        super().__init__(self.messgae)