from server.server import app
from logger import logging
from server.config import Config
import os


def create_uploads_path():
    if not os.path.exists(Config.upload_folder):
        logging.info(f"Creating upload folder: '%s'", Config.upload_folder)
        os.mkdir(Config.upload_folder)


create_uploads_path()
