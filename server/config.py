import os
from dataclasses import dataclass


@dataclass
class Config:

    # адрес на котором хостится сервер. Если будет указан "0.0.0.0", то распространится на все сетевые интерфейсы
    ip: str = "localhost"
    # порт, выбран 8999, т.к. не задевает дефолтные порты Windows и Unix подобных систем
    port: int = 8999
    # папка внутри проекта, в которую будет сохраняться датасет для классификации
    upload_folder: str = os.path.abspath("./server/uploads")
    # создание ключа сессии на основе процессорного рандома
    secret_key: bytes = os.urandom(10)
