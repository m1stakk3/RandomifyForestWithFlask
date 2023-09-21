import os
from logger import logging


def file_is_downloaded(path: str) -> bool:
    if os.path.exists(path):
        logging.info("File is downloaded!")
        return True
    logging.error("File was not downloaded!")
    return False
