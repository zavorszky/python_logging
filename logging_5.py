"""
Modern Python logging: Youtube: https://www.youtube.com/watch?v=9L77QExPmI0&list=PLcLIOuMu3bXrXGdqV7tPTU63a8sVjQDuw&index=30
4. példa
Logozás:
* hibák a stderr-re
* minden üzenet a napló fileba.
* - a file legyen json file
* Naplóírás sorkezelő/queue használattal
* A napló kiírás kiegészítése 'extra'-val
"""

import atexit
import logging
import logging.config


logger = logging.getLogger("logging_5")

logging_config2 = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)s: %(message)s",
        },
        "detailed": {
            "format": "[%(levelname)s|%(module)s|L%(lineno)d] %(asctime)s: %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%s",
        },
        "json": {
            "()": "logging_5_logger.MyJSONFormatter2",
            "fmt_keys": {
                "level": "levelname",
                "message": "message",
                "timestamp": "timestamp",
                "logger": "name",
                "module": "module",
                "function": "funcName",
                "line": "lineno",
                "thread_name": "threadName",
            },
        },
    },
    "handlers": {
        "stderr": {
            "class": "logging.StreamHandler",
            "level": "WARNING",
            "formatter": "simple",
            "stream": "ext://sys.stderr",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "json",
            "filename": "log/logging_5.log.json",
            "encoding": "utf-8",
            "maxBytes": 10000,
            "backupCount": 3,
        },
        "queue_handler": {
            "class": "logging.handlers.QueueHandler",
            "handlers": ["stderr", "file"],
            "respect_handler_level": True,
        },
    },
    "loggers": {"root": {"level": "DEBUG", "handlers": ["queue_handler"]}},
}


def main() -> None:
    logging.config.dictConfig(config=logging_config2)
    
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)

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
