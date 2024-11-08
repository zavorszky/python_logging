"""
Modern Python logging: Youtube: https://www.youtube.com/watch?v=9L77QExPmI0&list=PLcLIOuMu3bXrXGdqV7tPTU63a8sVjQDuw&index=30
4. példa
Logozás:
* hibák a stderr-re
* minden üzenet a napló fileba.
* - a file legyen json file

A logging_4.py-hoz tartozó MyJSONFormatter

Linkek:
Handling timezone in Python: geeksforgeeks: https://www.geeksforgeeks.org/handling-timezone-in-python/
"""

import datetime as dt
import pytz
import json
import logging
from typing import override


class MyJSONFormatter(logging.Formatter):
    def __init__(self, *, fmt_keys: dict[str, str] | None = None):
        super().__init__()
        self.fmt_keys = fmt_keys if fmt_keys is not None else {}

    @override
    def format(self, record: logging.LogRecord) -> str:
        message = self._prepare_log_dict(record)
        return json.dumps(message, default=str)

    def _prepare_log_dict(self, record: logging.LogRecord):
        always_fields = {
            "message": record.getMessage(),
#            "timestamp": dt.datetime.fromtimestamp(record.created, tz=dt.timezone.utc).isoformat(),
            "timestamp": dt.datetime.now(pytz.timezone("Europe/Budapest"))
        }

        if record.exc_info is not None:
            always_fields["stack_info"] = self.formatStack(record.stack_info)
        
        message = {
            key: msg_val if (msg_val := always_fields.pop(val, None)) is not None
            else getattr(record, val)
            for key, val in self.fmt_keys.items()
        }

        message.update(always_fields)

        return message