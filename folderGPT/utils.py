import logging
from datetime import datetime


RUN_ID = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

# Create a custom logger
class ProjectLogger(logging.Logger):
    def __init__(self, create_file: bool = False):
        super().__init__("folderGPT")

        # Set the format for the log messages
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s - %(levelname)s - %(message)s')

        # Create a stream to console handler to log the messages to a file
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setFormatter(self.formatter)
        self.addHandler(self.stream_handler)

        # Create a file handler to log the messages to a file if needed
        if create_file:
            self.file_handler = logging.FileHandler(f'logs/{RUN_ID}.txt')
            self.file_handler.setFormatter(self.formatter)
            self.addHandler(self.file_handler)
