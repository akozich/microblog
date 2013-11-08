__author__ = 'Aliaksei Kozich'

from .base import *

try:
    from .local import *
except ImportError:
    pass