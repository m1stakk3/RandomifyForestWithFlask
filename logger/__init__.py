import logging
import warnings


warnings.filterwarnings("ignore")
logging.basicConfig(
    filename="logs.log",
    filemode="w",
    encoding="utf-8",
    level=logging.INFO,
    format="%(name)s | %(levelname)s | %(message)s"
)
