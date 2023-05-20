# absteact class for all the file convertors
class FileConvertor:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def convert(self):
        raise NotImplementedError()