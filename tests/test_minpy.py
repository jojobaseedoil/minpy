import unittest
from minpy.omega import Omega

class TestMinpy(unittest.TestCase):
    def test_route(self):
        omega = Omega(16)
        self.assertTrue(omega.route(1, 3))
        self.assertFalse(omega.route(2, 3))

    def test_unroute(self):
        omega = Omega(16)
        omega.route(1, 3)
        self.assertTrue(omega.unroute(3))
        self.assertFalse(omega.unroute(3))

if __name__ == '__main__':
    unittest.main()
