""" Logging in Python

Logging is useful to track the error or exception or information. It also helps in debugging.
We use logging module to log the error.

Syntax:
import logging
from logging import *

basicConfig(**kwargs) Method

This method is used to config the logging system.

Syntax:
basicConfig(**kwargs)

filename : it specifies that a File handler be created, using the fileName rather than a Steam Handler.
filemode : if filename is specified, open the file in this mode. Defaults to 'a'. Write to 'w'
level : Set the root logger level to the specified level.
format : used the specified format string for the handler.
datefmt : use the specified date/time format, as accepted by time.strftime().
style : if format is specified,use this style for the format string. One of 
"""