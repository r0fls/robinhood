import unittest
import rh

class RobinTest(unittest.TestCase):
    def test(self):
        d = rh.robinhood(1)
        d.insert('te')
        d.insert('collisions are hard')
        self.assertEqual(2, len(d))
