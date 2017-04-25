import unittest 
import go_fish

class InitialDealTest(unittest.TestCase):
    def test(self):
        self.assertEqual(len(go_fish.initial_deal()), 7)
