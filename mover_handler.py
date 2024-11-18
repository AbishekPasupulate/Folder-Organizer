import logging
import os
from shutil import move
from os.path import splitext, exists, join
from watchdog.events import FileSystemEventHandler
from file_utils import make_unique, move_file


class MoverHandler(FileSystemEventHandler):
    def __init__(self, source_dir):
        self.source_dir = source_dir

    def ensure_dir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
            logging.info(f"Created directory: {path}")

    def move_to_dir(self, sub_dir, entry, name):
        dest = f"{self.source_dir}/{sub_dir}"
        self.ensure_dir(dest)
        move_file(dest, entry, name)
        logging.info(f"Moved {sub_dir.lower()} file: {name}")

    def on_modified(self, event):
        with os.scandir(self.source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_word(entry, name)
                self.check_document_pdf(entry, name)
                self.check_document_excel(entry, name)
                self.check_document_ppt(entry, name)
                self.check_zip_files(entry, name)
                self.check_executable_files(entry, name)
                self.check_c_files(entry, name)
                self.check_python_files(entry, name)

    def check_audio_files(self, entry, name):
        from extensions import audio_extensions
        for ext in audio_extensions:
            if name.endswith(ext) or name.endswith(ext.upper()):
                self.move_to_dir("Music", entry, name)

    def check_video_files(self, entry, name):
        from extensions import video_extensions
        for ext in video_extensions:
            if name.endswith(ext) or name.endswith(ext.upper()):
                self.move_to_dir("Videos", entry, name)

    def check_image_files(self, entry, name):
        from extensions import image_extensions
        for ext in image_extensions:
            if name.endswith(ext) or name.endswith(ext.upper()):
                self.move_to_dir("Images", entry, name)

    def check_document_word(self, entry, name):
        from extensions import document_extensions_word
        for ext in document_extensions_word:
            if name.endswith(ext) or name.endswith(ext.upper()):
                self.move_to_dir("Document/Word", entry, name)

    def check_document_pdf(self, entry, name):
        from extensions import document_extensions_pdf
        for ext in document_extensions_pdf:
            if name.endswith(ext) or name.endswith(ext.upper()):
                self.move_to_dir("Document/PDFs", entry, name)

    def check_document_excel(self, entry, name):
        from extensions import document_extensions_excel
        for ext in document_extensions_excel:
            if name.endswith(ext) or name.endswith(ext.upper()):
                self.move_to_dir("Document/Excell", entry, name)

    def check_document_ppt(self, entry, name):
        from extensions import document_extensions_ppt
        for ext in document_extensions_ppt:
            if name.endswith(ext) or name.endswith(ext.upper()):
                self.move_to_dir("Document/PPTs", entry, name)

    def check_zip_files(self, entry, name):
        from extensions import zip_File
        for ext in zip_File:
            if name.endswith(ext) or name.endswith(ext.upper()):
                self.move_to_dir("Archives", entry, name)

    def check_executable_files(self, entry, name):
        from extensions import appications
        for ext in appications:
            if name.endswith(ext) or name.endswith(ext.upper()):
                self.move_to_dir("Applications", entry, name)

    def check_c_files(self, entry, name):
        from extensions import c_file
        for ext in c_file:
            if name.endswith(ext) or name.endswith(ext.upper()):
                self.move_to_dir("C_Files", entry, name)


    def check_python_files(self, entry, name):
        from extensions import python_file
        for ext in python_file:
            if name.endswith(ext) or name.endswith(ext.upper()):
                self.move_to_dir("Python_Files", entry, name)

