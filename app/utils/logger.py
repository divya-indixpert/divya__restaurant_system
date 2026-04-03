import logging
import os

LOG_FILE = "app/utils/log.txt"

def get_logger():

 
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    logger = logging.getLogger("RestaurantSystem")
    logger.setLevel(logging.INFO)

    if not logger.handlers:

        file_handler = logging.FileHandler(LOG_FILE)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger