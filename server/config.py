import os
from dataclasses import dataclass


@dataclass
class Config:

    ip: str = "localhost"
    port: int = 8999
    upload_folder: str = os.path.abspath("./server/uploads")
    secret_key = os.urandom(10)

    if not os.path.exists(upload_folder):
        os.mkdir(upload_folder)
