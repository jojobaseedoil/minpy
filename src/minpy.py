import ctypes

lib = ctypes.cdll.LoadLibrary('./libminpy.so')

class Omega(object):

    def __init__(self, n, extras=0, radix=4):

        lib.Omega_new.argtypes = [
            ctypes.c_int, 
            ctypes.c_int, 
            ctypes.c_int, 
        ]
        lib.Omega_new.restype = ctypes.c_void_p

        lib.Omega_route.argtypes = [
            ctypes.c_void_p,
            ctypes.c_int,
            ctypes.c_int
        ]
        lib.Omega_route.restype = ctypes.c_bool

        lib.Multistage_clear.argtypes = [
            ctypes.c_void_p
        ]
        lib.Multistage_clear.restype = ctypes.c_void_p

        lib.Multistage_show.argtypes = [
            ctypes.c_void_p
        ]
        lib.Multistage_show.restype = ctypes.c_void_p

        self.obj = lib.Omega_new(n, extras, radix)

    def route(self, input, output):
        return lib.Omega_route(self.obj, input, output)
    
    def show(self):
        lib.Multistage_show(self.obj)

    def clear(self):
        lib.Multistage_clear(self.obj)