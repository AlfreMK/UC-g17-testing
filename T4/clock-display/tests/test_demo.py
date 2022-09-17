from src.clock_factory import *
from src.clock_display import *
from unittest import TestCase
#import unittest # for skipping tests

class TestDemo(TestCase):

    def setUp(self):
        self.factory = ClockFactory()
        self.factory_2 = ClockFactory()
        self.factory_3 = ClockFactory()
        self.clock = self.factory.create("hh:mm")
        self.clock_2 = self.factory_2.create("hh:mm:ss")
        self.clock_3 = self.factory_3.create("hh:mm:ss:mmmm")

    def test_factory_1(self):
        self.assertEqual(self.factory.create("hh:mm").str(), "00:00")
    
    def test_factory_2(self):
        self.assertEqual(self.factory_2.create("hh:mm:ss").str(), "00:00:00")
    
    def test_factory_3(self):
        self.assertEqual(self.factory_3.create("hh:mm:ss:mmmm").str(), "00:00:00:00")
    
    def tearDown(self):
        pass
    
    # ignore this test for now
    #@unittest.skip("skipping test")
    def test_demo(self):
        for i in range(10000):
            self.clock.increment()
            # print(self.clock.str())

    def test_str(self):
        self.assertEqual(self.clock.str(), "00:00")
        

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

    def test_clone(self):
        for i in range(10000):
            self.clock.increment()
        clone = self.clock.clone()
        self.assertEqual(self.clock.str(), clone.str())

    def test_increment(self):
        for i in range(24*60):
            self.clock.increment()
        self.assertEqual(self.clock.str(), "00:00")
    
    def test_increment_2(self):
        for i in range(86400): # 86400 seconds = 24 hours
            self.clock_2.increment()
        self.assertEqual(self.clock_2.str(), "00:00:00")

    def test_increment_3(self):
        for i in range(10000): # 10000 milliseconds = 10 seconds
            self.clock_3.increment()
        self.assertEqual(self.clock_3.str(), "00:00:10:00")
    