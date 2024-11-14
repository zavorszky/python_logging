"""
Modern Python logging: Youtube: https://www.youtube.com/watch?v=9L77QExPmI0&list=PLcLIOuMu3bXrXGdqV7tPTU63a8sVjQDuw&index=30
4. példa
Logozás:
* hibák a stderr-re
* minden üzenet a napló fileba.
* - a file legyen json file
* Naplóírás sorkezelő/queue használattal
* A napló kiírás kiegészítése 'extra'-val

A logging_5.py-höz tartozó MyJSONFormatter

Linkek:
Handling timezone in Python: geeksforgeeks: https://www.geeksforgeeks.org/handling-timezone-in-python/
"""

import datetime as dt
import pytz
import json
import logging
from typing import override

TZ_EUROPE_BUDAPEST = pytz.timezone("Europe/Budapest")

# Az alábbi kulcsszavak előállítása a 'expe_LogRecord.py'-ban.
# lr = logging.LogRecord(....)
# all_attributes = dir(lr)
# print(all_attributes)
LOG_RECORD_BUILTIN_ATTRS = [
    "__class__",
    "__delattr__",
    "__dict__",
    "__dir__",
    "__doc__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getattribute__",
    "__getstate__",
    "__gt__",
    "__hash__",
    "__init__",
    "__init_subclass__",
    "__le__",
    "__lt__",
    "__module__",
    "__ne__",
    "__new__",
    "__reduce__",
    "__reduce_ex__",
    "__repr__",
    "__setattr__",
    "__sizeof__",
    "__str__",
    "__subclasshook__",
    "__weakref__",
    "args",
    "created",
    "exc_info",
    "exc_text",
    "filename",
    "funcName",
    "getMessage",
    "levelname",
    "levelno",
    "lineno",
    "module",
    "msecs",
    "msg",
    "name",
    "pathname",
    "process",
    "processName",
    "relativeCreated",
    "stack_info",
    "taskName",
    "thread",
    "threadName",
]


class MyJSONFormatter2(logging.Formatter):
    def __init__(self, *, fmt_keys: dict[str, str] | None = None):
        super().__init__()
        self.fmt_keys = fmt_keys if fmt_keys is not None else {}

    # @override
    def format(self, record: logging.LogRecord) -> str:
        message = self._prepare_log_dict(record)
        # Figyelem!
        # Az 'emsure_ascii' paraméter alapértelmezés szerint 'True',
        # de akkor az ékezetes karakterek nem jelennek meg, csak a kódjuk:
        # pl.: 'ü' helyett a '\u00fc' karakter sorozat.
        # Ha 'False', akkor jó a file-ban is a szöveg.
        return json.dumps(message, ensure_ascii=False, default=str)

    def _prepare_log_dict(self, record: logging.LogRecord):
        always_fields: dict = {
            "message": record.getMessage(),
            "timestamp": dt.datetime.fromtimestamp(
                record.created, tz=TZ_EUROPE_BUDAPEST
            ).isoformat(),
        }

        if record.exc_info is not None:
            always_fields["exc_info"] = self.formatException(record.exc_info)

        if record.stack_info is not None:
            always_fields["stack_info"] = self.formatStack(record.stack_info)

        # message = {
        #    key: msg_val if (msg_val := always_fields.pop(val, None)) is not None
        #    else getattr(record, val)
        #    for key, val in self.fmt_keys.items()
        # }
        message: dict = always_fields
        for key, val in self.fmt_keys.items():
            # key: A message-ben szereplő kulcs.
            # val: Ez a record metódust kell hívni.
            try:
                msg_val = getattr(record, val)
            except Exception:
                msg_val = None

            if msg_val is not None:
                message[key] = msg_val

        for key2, val2 in record.__dict__.items():
            if key2 not in LOG_RECORD_BUILTIN_ATTRS:
                message[key2] = val2

        return message
