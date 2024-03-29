from src.clock_factory import *
from src.clock_display import *
from unittest import TestCase

class TestDemo(TestCase):
# TESTS FOR MUTATEST
    def setUp(self):
        self.factory = ClockFactory()
        self.factory_2 = ClockFactory()
        self.factory_3 = ClockFactory()
        self.clock = self.factory.create("hh:mm")
        self.clock_2 = self.factory_2.create("hh:mm:ss")
        self.clock_3 = self.factory_3.create("hh:mm:ss:mmmm")
        self.environment_is_clean()

    def environment_is_clean(self):
        try:
            number = NumberDisplay(2,5)
            number.increase()
            self.assertEqual(number.value, 3)
        except AssertionError:
            raise

    def test_noneToFalse(self):
        # mutatest:
        #   src/clock_display.py: (l: 4, c: 38) - mutation from None to False
        self.assertEqual(ClockDisplay([24]).__init__([24]), None)
    
    def test_annotations_clock_d(self):
        # mutatest:
        #   src/clock_display.py: (l: 4, c: 38) - mutation from None to False
        self.assertEqual(ClockDisplay.__init__.__annotations__["return"], None)
    
    def test_annotations_display_number(self):
        # mutatest:
        #   src/clock_display.py: (l: 4, c: 38) - mutation from None to False
        self.assertEqual(NumberDisplay.__init__.__annotations__["return"], None)
    
    def test_annotations_clock_factory(self):
        # mutatest:
        #   src/clock_display.py: (l: 4, c: 38) - mutation from None to False
        self.assertEqual(ClockFactory.__init__.__annotations__["return"], None)

    def test_increment_gte(self):
        # mutatest:
        #   src/clock_display.py: (l: 9, c: 14) - mutation from <class '_ast.GtE'> to <class '_ast.Gt'>
        factory_test = ClockFactory()
        factory_test.cache["hh"] = ClockDisplay([24])
        clock_test = factory_test.create("hh")
        for i in range(10):
            clock_test.increment()
        self.assertEqual(clock_test.str(), "10")

    def test_noneToFalse2(self):
        # mutatest:
        #   src/display_number.py: (l: 3, c: 41) - mutation from None to False
        self.assertEqual(NumberDisplay(0,60).__init__(0,60), None)

    
    def test_increase_add_mod(self):
        # mutatest:
        #   src/display_number.py: (l: 9, c: 23) - mutation from <class '_ast.Add'> to <class '_ast.Sub'>
        number = NumberDisplay(0,60)
        number.value = 10
        number.increase()
        self.assertEqual(number.str(), "11")

    def test_lt_neq(self):
        # mutatest:
        #   src/display_number.py: (l: 17, c: 11) - mutation from <class '_ast.LtE'> to <class '_ast.NotEq'>
        number = NumberDisplay(0,60)
        number.value = 50
        self.assertEqual(number.str(), "50")
    
    def test_invariant_lt_neq(self):
        # mutatest:
        #   src/display_number.py: (l: 22, c: 15) - mutation from <class '_ast.Lt'> to <class '_ast.NotEq'>
        number = NumberDisplay(65,60)
        self.assertEqual(number.invariant(), False)
    
    def test_invariant_lt_neq_2(self):
        # mutatest:
        #   src/display_number.py: (l: 22, c: 15) - mutation from <class '_ast.Lt'> to <class '_ast.NotEq'>
        number = NumberDisplay(35,60)
        self.assertEqual(number.invariant(), True)
    
    def test_invariant_lt_lte(self):
        # mutatest:
        #   src/display_number.py: (l: 22, c: 15) - mutation from <class '_ast.Lt'> to <class '_ast.Lte'>
        number = NumberDisplay(60,60)
        number.value = 60
        self.assertEqual(number.invariant(), False)

    def test_oder_op(self):
        number = self.clock.numbers[0]
        newNumber = number.clone()
        limit = 0.4
        value = 1
        newNumber.limit = limit
        newNumber.value = value
        newNumber.increase()
        self.assertEqual(newNumber.value,  (value + limit + 1) % limit)
    
    def test_oder_op_2(self):
        number = self.clock.numbers[0]
        newNumber = number.clone()
        limit = -1
        value = -5
        newNumber.limit = limit
        newNumber.value = value
        newNumber.increase()
        self.assertEqual(newNumber.value,  (value + limit + 1) % limit)


# RUN MUTATESTS (inside clock-display) WITH :
# mutatest -s . -t "pytest" -r 314

# RUN COVERAGE:
# coverage run -m unittest discover
# coverage html