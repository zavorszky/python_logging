"""
Modern Python logging: Youtube: https://www.youtube.com/watch?v=9L77QExPmI0&list=PLcLIOuMu3bXrXGdqV7tPTU63a8sVjQDuw&index=30
4. példa
Logozás:
* hibák a stderr-re
* minden üzenet a napló fileba.
* - a file legyen json file
"""


import logging
import logging.config


logger = logging.getLogger("logging_4")

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "simple": {
            "format": "%(levelname)s: %(message)s",
        },
        "detailed":{
            "format": "[%(levelname)s|%(module)s|L%(lineno)d] %(asctime)s: %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%s"
        },
        "json": {
            "()": "logging_4_logger.MyJSONFormatter",
            "fmt_keys": {
                "level": "levelname",
                "message": "message",
                "timestamp": "timestamp",
                "logger": "name",
                "module": "module",
                "line": "lineno",
                "thread_name": "threadName"
            }
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
            "formatter": "json",
            "filename": "log/logging_4.log.json",
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
    logging.config.dictConfig(config = logging_config)

    logger.debug("Debug uzenet")
    logger.info("Info uzenet")
    logger.warning("Warning uzenet")
    logger.error("Error uzenet")
    logger.critical("Critical uzenet")
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("Exception uzenet")


if __name__ == "__main__":
    main()
