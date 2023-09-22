import os
import time
from dataclasses import dataclass

from PyPDF2 import PdfReader, PdfWriter


@dataclass
class AppendPdfToPdf:
    path_original_file: str
    path_file_to_append: str
    path_output: str

    def append(self) -> None:
        original_file = open(self.path_original_file, "rb")
        file_to_append = open(self.path_file_to_append, "rb")

        writer = PdfWriter()

        self._add_pages(writer, PdfReader(original_file, strict=False))
        self._add_pages(writer, PdfReader(file_to_append, strict=False))

        with open(self.path_output, "wb") as output_file:
            writer.write(output_file)

        while not os.path.exists(self.path_output):
            time.sleep(0.1)

    def _add_pages(self, pdf_writer, pdf_reader) -> PdfWriter:
        for n in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[n])
        return pdf_writer
