"""
A logging.LogRecord mező nevei (a '__' karaktereket tartalmazó nevek nélkül).
args
created
exc_info
exc_text
filename
funcName
getMessage
levelname
levelno
lineno
module
msecs
msg
name
pathname
process
processName
relativeCreated
stack_info
taskName
thread
threadName
"""

import logging

lr = logging.LogRecord("logger_name", 0, "c:/log_dir", 101, "bbbbbb", ["arg_0","arg_1"], None, "funtion_name","sinfo")
print(lr)

print("")
all_attributes = dir(lr)
print(all_attributes)

print("")
filtered_attributes = [a for a in all_attributes if "__" not in a]
print(filtered_attributes)

print("")
for item in filtered_attributes:
    print(item)

