import ctypes
import os

# Load the shared library
lib = ctypes.CDLL(os.path.abspath('build/libminpy.so'))

# Define the Multistage class
class Multistage:
    def __init__(self, size, extras=0, radix=4):
        lib.Multistage_new.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
        lib.Multistage_new.restype = ctypes.c_void_p
        self.obj = lib.Multistage_new(size, extras, radix)

        self.__SIZE   = size
        self.__EXTRAS = extras
        self.__RADIX  = radix

        lib.Multistage_get_stages.argtypes = [ctypes.c_void_p]
        lib.Multistage_get_stages.restype = ctypes.c_int
        self.__STAGES = lib.Multistage_get_stages(self.obj)

    def clear(self):
        lib.Multistage_clear.argtypes = [ctypes.c_void_p]
        lib.Multistage_clear(self.obj)

    def show(self):
        lib.Multistage_show.argtypes = [ctypes.c_void_p]
        lib.Multistage_show(self.obj)
    
    def __len__(self):
        return self.__SIZE

    @property
    def stages(self):
        return self.__STAGES

    def shape(self):
        return (self.__SIZE, self.__STAGES)

# Define the Slider class
class Slider:
    def __init__(self, size, extras, radix):
        lib.Slider_new.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
        lib.Slider_new.restype = ctypes.c_void_p
        self.obj = lib.Slider_new(size, extras, radix)

    # Add more methods here

# Define the Omega class
class Omega(Multistage):
    def __init__(self, size, extras=0, radix=4):
        super().__init__(size, extras, radix)
        lib.Omega_new.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
        lib.Omega_new.restype = ctypes.c_void_p
        self.obj = lib.Omega_new(size, extras, radix)

    def route(self, input, output):
        lib.Omega_route.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
        lib.Omega_route.restype = ctypes.c_bool
        return lib.Omega_route(self.obj, input, output)

    def unroute(self, output):
        lib.Omega_unroute.argtypes = [ctypes.c_void_p, ctypes.c_int]
        lib.Omega_unroute.restype = ctypes.c_bool
        return lib.Omega_unroute(self.obj, output)