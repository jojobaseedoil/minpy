import unittest
from minpy import Multistage, Slider, Omega

class TestMinpy(unittest.TestCase):

    def test_multistage(self):
        ms = Multistage(8)
        self.assertEqual(ms.shape(), (8, 3))
        ms.clear()
        self.assertEqual(ms._min.sum(), 0)

    def test_slider(self):
        sl = Slider(8, 1, 4)
        self.assertEqual(sl.slide(0b1100, 1), 0b0110)
        self.assertEqual(sl.concat(0b10, 0b01, 0b11), 0b110110)

    def test_omega(self):
        om = Omega(8)
        self.assertTrue(om.route(0, 7))
        self.assertTrue(om.unroute(7))
        self.assertFalse(om.unroute(7))

if __name__ == '__main__':
    unittest.main()