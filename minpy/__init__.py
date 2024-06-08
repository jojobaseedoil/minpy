# minpy/__init__.py

from .omega import Multistage, Omega

import os
import ctypes

lib_path = os.path.join(os.path.dirname(__file__), 'libminpy.so')
ctypes.CDLL(lib_path)
