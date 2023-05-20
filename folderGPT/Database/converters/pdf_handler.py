import os
from typing import Optional

import PyPDF2
import docx

from folderGPT.Database.converters.general_convertor import FileConvertor


class PDFConvertor(FileConvertor):

    def __init__(self, file_name: str, mode: str = "keep"):
        super().__init__(file_name)
        self.mode = mode

    @staticmethod
    def pdf_to_docx(pdf_file_name: str, docx_file_name: Optional[str] = None) -> docx.Document:
        """
        Convert a PDF file to a DOCX file
        :param pdf_file_name: name of the PDF file
        :param docx_file_name:  name of the DOCX file
        :param mode: save mode, can be "keep" or "replace"
        :return:
        """
        # get file name from path
        if docx_file_name is None:
            docx_file_name = pdf_file_name.split("\\")[-1].replace(".pdf", ".docs")

        # Read the text from the PDF file
        with open(pdf_file_name, "rb") as f:
            pdf_reader = PyPDF2.PdfFileReader(f)
            text = ""
            for page in pdf_reader.pages:
                text += page.extractText()

        # Create a Docs document
        doc = docx.Document()

        # Add the text to the Docs document
        doc.add_paragraph(text)

        # Save the Docs document in the fileDataBase
        return doc

    def convert(self):
        return PDFConvertor.pdf_to_docx(self.file_name)


def convert_all_pdf_in_folder_to_docx(folder_path: str):
    # Get all the PDF files paths in the folder_path
    pdf_files = [
        os.path.join(folder_path, file_name)
        for file_name in os.listdir(folder_path)
        if file_name.endswith(".pdf")
    ]
    # convert all the PDF files to DOCX files and store them in the same folder
    for pdf_file in pdf_files:
        PDFConvertor.pdf_to_docx(pdf_file)
