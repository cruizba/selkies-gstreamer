import ctypes

import logging
logger = logging.getLogger("xorg")
logger.setLevel(logging.INFO)

class Xorg:
    def __init__(self, display_name):
        # Load the shared library
        self.libxorg = ctypes.CDLL('/usr/local/lib/selkies-xorg-iface/xorg.so')

        # Define the argument and return types for the functions you need
        self.libxorg.XDisplayOpen.argtypes = [ctypes.c_char_p]
        self.libxorg.XDisplayOpen.restype = ctypes.c_int

        self.libxorg.XKey.argtypes = [ctypes.c_ulong, ctypes.c_int]
        self.libxorg.XKey.restype = None

        success = self.libxorg.XDisplayOpen(str.encode(display_name))
        if success != 0:
            raise RuntimeError("Failed to open display")
    
    def key_up(self, keysym):
        try:
            self.libxorg.XKey(keysym, 0)
        except Exception as e:
            logger.warning("Failed to send key up event: %s" % e)
    
    def key_down(self, keysym):
        try:
            self.libxorg.XKey(keysym, 1)
        except Exception as e:
            logger.warning("Failed to send key down event: %s" % e)
    
