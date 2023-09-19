import logging


logging.basicConfig(
    filename="logs.log",
    filemode="w",
    encoding="utf-8",
    level=logging.INFO,
    format="%(name)s | %(levelname)-8s | %(message)s'"
)
