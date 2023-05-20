import os
from enum import Enum

import docx

from folderGPT.Database.converters.pdf_handler import PDFConvertor
from folderGPT.utils import ProjectLogger

DATABASE_PATH = ""


# MODE ENUM CLASS FOR DATABASE
class Mode(Enum):
    KEEP = "keep"
    REPLACE = "replace"

    # get all enum values method
    @classmethod
    def get_all(cls):
        return [mode.value for mode in cls]


class FileDatabase:
    local_path: str = os.path.dirname(os.path.abspath(__file__))
    file_data_base_path = os.path.join(local_path, "file_data_base/")
    linked_folders = []

    def __init__(self):
        # check if file_data_base_path exist, if not create the folder
        if not self.check_if_document_exists():
            os.makedirs(self.file_data_base_path)

    def check_if_document_exists(self, file_name: str =''):
        return os.path.exists(f"{self.file_data_base_path}/{file_name}")

    def add_document(self, document: docx.Document, file_name: str, mode: str = "keep"):
        """
        Add a document to the file database
        :param document: docx.Document object to be added
        :param file_name: str name of the file
        :param mode: can be "keep" or "replace", if keep and file exists, raise error, if replaced, replace the file
        :return:
        """

        if not file_name.endswith(".docx"):
            file_name = file_name.split('.')[0] + ".docx"

        file_exists = self.check_if_document_exists(file_name)

        # check if mode valid
        if mode not in Mode.get_all():
            raise ValueError(f"Invalid mode {mode}")
        #
        if mode == "keep":
            if file_exists:
                ProjectLogger().info(f"File {file_name} already exists")
                return

        document.save(f"{self.file_data_base_path}/{file_name}")
        ProjectLogger().info(f"add file {file_name} to DB")

    def upload_folder(self, folder_path: str, mode: str = "keep"):
        # Get all the PDF files paths in the folder_path
        pdf_files_paths = [
            os.path.join(folder_path, file_name)
            for file_name in os.listdir(folder_path)
            if file_name.endswith(".pdf")
        ]
        # convert all the PDF files to DOCX files and store them in the same folder
        for pdf_file_path in pdf_files_paths:
            pdf_file_name = os.path.basename(pdf_file_path)
            self.add_document(PDFConvertor(pdf_file_path).convert(), pdf_file_name, mode=mode)

    def update(self):
        ProjectLogger().info("Updating file database")
        for folder in self.linked_folders:
            self.upload_folder(folder)

    def add_folder(self, other):
        self.linked_folders.append(other)
        return self
