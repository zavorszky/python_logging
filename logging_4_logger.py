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

TZ_EUROPE_BUDAPEST = pytz.timezone("Europe/Budapest")


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
#            "timestamp": dt.datetime.now(pytz.timezone("Europe/Budapest")),
            "timestamp": dt.datetime.fromtimestamp(record.created, tz=TZ_EUROPE_BUDAPEST).isoformat(),
        }

        if record.exc_info is not None:
            always_fields["exc_info"] = self.formatException(record.exc_info)

        if record.stack_info is not None:
            always_fields["stack_info"] = self.formatStack(record.stack_info)

        message = {
            key: msg_val if (msg_val := always_fields.pop(val, None)) is not None
            else getattr(record, val)
            for key, val in self.fmt_keys.items()
        }

        message.update(always_fields)

        return message


class MyJSONFormatter2(logging.Formatter):
    def __init__(self, *, fmt_keys: dict[str, str] | None = None):
        super().__init__()
        self.fmt_keys = fmt_keys if fmt_keys is not None else {}

    #@override
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

        return message
