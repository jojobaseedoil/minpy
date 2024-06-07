from math import ceil, pow
import numpy as np
from numba import jit
from .multistage import Multistage
from .slider import Slider

class Omega(Multistage):
    """Class representing a routing algorithm based on a multistage network."""

    def __init__(self, size: np.uint, extras: np.uint=0, radix: np.uint=4) -> None:
        """
        Constructor of the class.

        Args:
            size   (np.uint): Size of the multistage network.
            extras (np.uint, optional): Number of extra stages. Default is 0.
            radix  (np.uint, optional): Number of switch ports. Default is 4.
        """
        super().__init__(size, extras, radix)

        # Initialization of the sliding window and extra codes
        self.__WINDOW      : Slider = Slider(size, extras, radix)
        self.__EXTRA_CODES : list   = [i for i in range(ceil(pow(radix, extras)))]

    @jit
    def route(self, input: int, output: int) -> bool:
        """
        Routes a message from input to output.

        Args:
            input  (int): Input index.
            output (int): Output index.

        Returns:
            bool: True if routing is successful, False otherwise.
        """
        assert 0 <= input  < len(self), f"Index {input} out of range."
        assert 0 <= output < len(self), f"Index {output} out of range."

        if output in self._routed:
            return True

        paths = [self.__WINDOW.concat(input, extra, output) for extra in self.__EXTRA_CODES]

        for path in paths:
            if self.__is_path_available(path):
                self._routed[output] = path
                self.__send_message(path)
                return True

        return False
    
    @jit
    def __is_path_available(self, path: int) -> bool:
        """
        Checks if a path is available for the given path.

        Args:
            path (int): Binary Path.

        Returns:
            bool: True if the path is available, False otherwise.
        """
        for col in range(self.stages):
            row = self.__WINDOW.slide(path, col + 1)
            if not self.__is_available(path, row, col):
                return False
        return True

    def unroute(self, output: int) -> bool:
        """
        Unroutes a message from the output.

        Args:
            output (int): Output index.

        Returns:
            bool: True if unroute is successful, False otherwise.
        """
        assert 0 <= output < len(self), f"Index {output} out of range."

        if output not in self._routed:
            return False

        path: int = self._routed[output]

        for col in range(self.stages):

            row : int = self.__WINDOW.slide(path, col + 1)
            idx : int = row * self.stages + col

            self._min[idx] = max(0, self._min[idx] - 1)

            if self._min[idx] == 0:
                self._swt[idx] = -1

        del self._routed[output]

        return True

    def __is_available(self, path: int, row: int, col: int) -> bool:
        """
        Checks if a path is available.

        Args:
            path (int): Binary Path.
            row  (int): Row index.
            col  (int): Column index.

        Returns:
            bool: True if the path is available, False otherwise.
        """
        is_free      : bool = self._min[row * self.stages + col] == 0
        is_multicast : bool = self._swt[row * self.stages + col] == self.__WINDOW.source(path, col + 1)

        return is_free or is_multicast

    def __send_message(self, path: int) -> None:
        """
        Sends a message through the path.

        Args:
            path (int): Binary Path.
        """
        for col in range(self.stages):

            row: int = self.__WINDOW.slide(path, col + 1)

            self._min[row * self.stages + col] += 1
            self._swt[row * self.stages + col]  = self.__WINDOW.source(path, col)