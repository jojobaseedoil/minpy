from math import ceil, log2
import numpy as np

class Slider:
    """Class to represent a sliding window operation."""

    def __init__(self, size: np.uint, extras: np.uint, radix: np.uint) -> None:
        """
        Constructor of the class.

        Args:
            size   (np.uint): Size of the sliding window.
            extras (np.uint): Number of extra bits.
            radix  (np.uint): Radix of the sliding operation.
        """
        # Calculation of various bit lengths and masks
        self.__WIN_BITS  : np.uint = ceil(log2(size))
        self.__EXT_BITS  : np.uint = ceil(radix/2) * extras
        self.__WORD_BITS : np.uint = 2 * self.__WIN_BITS + self.__EXT_BITS

        # Masks for window and source operations
        self.__WIN_MASK : np.uint = size - 1
        self.__SRC_MASK : np.uint = radix - 1

        # Rate of sliding operation
        self.__SLIDE_RATE : np.uint = ceil(radix/2)

    def slide(self, word: np.uint, col: np.uint) -> np.uint:
        """
        Slides the window over the word.

        Args:
            word (np.uint): Input word.
            col  (np.uint): Column index.

        Returns:
            np.uint: Slided window.
        """
        return word >> (self.__WORD_BITS - col * self.__SLIDE_RATE - self.__WIN_BITS) & self.__WIN_MASK

    def concat(self, begin: np.uint, middle: np.uint, end: np.uint) -> np.uint:
        """
        Concatenates three parts into one word.

        Args:
            begin  (np.uint): Begin part.
            middle (np.uint): Middle part.
            end    (np.uint): End part.

        Returns:
            np.uint: Concatenated word.
        """
        return end | middle << self.__WIN_BITS | begin << (self.__WIN_BITS + self.__EXT_BITS)

    def source(self, word: np.uint, col: np.uint) -> np.uint:
        """
        Extracts the source from the word.

        Args:
            word (np.uint): Input word.
            col  (np.uint): Column index.

        Returns:
            np.uint: Extracted source.
        """
        return word >> (self.__WORD_BITS - col * self.__SLIDE_RATE) & self.__SRC_MASK
