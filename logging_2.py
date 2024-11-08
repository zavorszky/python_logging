"""
Youtube: Modern Python logging.
https://www.youtube.com/watch?v=9L77QExPmI0&list=PLcLIOuMu3bXrXGdqV7tPTU63a8sVjQDuw&index=30
2. példa
Logozás:
* hibák a stderr-re
* minden üzenet a napló fileba.
"""

import logging
import logging.config

logger = logging.getLogger("logging_2")

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)s: %(message)s",
        }
    },
    "handlers": {
        "stderr": {
            "class":"logging.StreamHandler",
            "level": "WARNING",
            "formatter": "simple",
            "stream": "ext://sys.stderr",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filename": "log/logging_2.log",
            "encoding": "UTF-8",
            "maxBytes": 10000,
            "backupCount": 3,
        }
    },
    "loggers": {
        "root": {
            "level": "DEBUG",
            "handlers": [
                "stderr",
                "file",
            ]
        }
    },
}


def main() -> None:
    logging.config.dictConfig(config=logging_config)

    logger.debug("Debug üzenet")
    logger.info("Info üzenet")
    logger.warning("Warning üzenet")
    logger.error("Error üzenet")
    logger.critical("Critical üzenet")
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("Exception üzenet")


if __name__ == "__main__":
    main()
