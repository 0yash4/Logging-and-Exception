import logging
import os
from datetime import datetime

LOG_FILE="Logging/Logging_info.log"


logging.basicConfig(
    filename=LOG_FILE,
    format="[ %(asctime)s ] - %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


if __name__=="__main__":
    logging.warning("Half-way through logging")
    logging.info("This is Info")