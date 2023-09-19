import os


def file_is_downloaded(path: str) -> bool:
    if os.path.exists(path):
        return True
    return False
