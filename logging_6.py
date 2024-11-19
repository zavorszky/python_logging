"""
Modern Python logging: Youtube: https://www.youtube.com/watch?v=9L77QExPmI0&list=PLcLIOuMu3bXrXGdqV7tPTU63a8sVjQDuw&index=30
6. példa
Logozás:
* hibák a stderr-re
* minden üzenet a napló fileba.
* - a file legyen json file
* Naplóírás sorkezelő/queue használattal
* A napló kiírás kiegészítése 'extra'-val
* A 'logging' konfigurálása konfigurációs file-al.
"""

import atexit
import logging
import logging.config
import pathlib
import json


logger = logging.getLogger("logging_6")


def logging_setup() -> None:
    config_file = pathlib.Path("logging_6.config.json")
    with open(config_file) as f:
        config = json.load(f)
    logging.config.dictConfig(config)

    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)


def main() -> None:
    logging_setup()

    logger.debug("Debug üzenet")
    logger.info("Info üzenet", extra={"x1": 1, "x2": "ez az x2"})
    logger.warning("Warning üzenet", extra={"x1": 1, "x2": "ez az x2"})
    logger.error("Error üzenet")
    logger.critical("Critical üzenet")
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("Exception üzenet")


# -----------------------------------------------

if __name__ == "__main__":
    main()
