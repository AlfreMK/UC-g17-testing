from src.clock_factory import *
from unittest import TestCase
#import unittest # for skipping tests

class TestDemo(TestCase):

    def setUp(self):
        self.factory = ClockFactory()
        self.clock = self.factory.create("hh:mm")

    def tearDown(self):
        pass
    
    # ignore this test for now
    #@unittest.skip("skipping test")
    def test_demo(self):
        for i in range(10000):
            self.clock.increment()
            print(self.clock.str())

    def test_invariant(self):
        for i in range(10000):
            self.clock.increment()
            self.assertTrue(self.clock.invariant())
    
    def test_reset(self):
        for i in range(10000):
            self.clock.increment()
        
        for i in self.clock.numbers:
            i.reset()
            self.assertEqual(i.value, 0)
        