"""
Youtube: Modern Python logging.
https://www.youtube.com/watch?v=9L77QExPmI0&list=PLcLIOuMu3bXrXGdqV7tPTU63a8sVjQDuw&index=30
1. példa
Naplozás a stdout-ra.
"""

import logging
import logging.config

logger = logging.getLogger("logging_1")

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    # "filters":{},
    "formatters": {
        "simple": {
            "format": "%(levelname)s: %(message)s",
        }
    },
    "handlers": {
        "stdout": {
            "class":"logging.StreamHandler",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        }
    },
    "loggers": {

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
