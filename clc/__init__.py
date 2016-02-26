import os
from clc import Client, Config

if os.environ.get("DEBUG"):
    import logging
    logging.basicConfig(level=logging.DEBUG)
    l = logging.getLogger('requests')
    l.setLevel(logging.DEBUG)
    l = logging.getLogger('urllib3')
    l.setLevel(logging.DEBUG)
    l.propagate = True
    import httplib
    httplib.HTTPConnection.debuglevel = 1


