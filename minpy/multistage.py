from math import ceil, log
import numpy as np

class Multistage:
    """Class to represent a multi-stage structure."""

    def __init__(self, size: np.uint, extras: np.uint=0, radix: np.uint=4) -> None:
        """
        Constructor of the class.

        Args:
            size   (np.uint): Size of the structure.
            extras (np.uint, optional): Number of extra stages. Default is 0.
            radix  (np.uint, optional): Number of switch ports. Default is 4.
        """
        # Initialization of the structure parameters
        self._SIZE   : np.uint = size
        self._EXTRAS : np.uint = extras
        self._RADIX  : np.uint = radix
        self._STAGES : np.uint = ceil(log(size, radix)) + extras

        # Initialization of internal variables
        self._min    = None
        self._swt    = None
        self._routed = None

        # Clearing the structure
        self.clear()

    def clear(self) -> None:
        """Clears the structure, resetting its internal variables."""
        self._min = np.zeros(shape=(self._SIZE * self._STAGES), dtype=np.uint)
        self._swt = np.full(shape=(self._SIZE * self._STAGES), dtype=np.int32, fill_value=-1)
        self._routed = {}

    def __len__(self) -> np.uint:
        """Returns the size of the structure."""
        return self._SIZE

    def shape(self) -> tuple:
        """Returns the shape of the structure."""
        return (self._SIZE, self._STAGES)

    @property
    def stages(self) -> np.uint:
        """Returns the number of stages of the structure."""
        return self._STAGES

    def show(self) -> None:
        """Prints a visual representation of the structure."""
        for i in range(len(self)):
            for j in range(self.stages):
                print(self._min[i * self.stages + j], end=' ')
            print()