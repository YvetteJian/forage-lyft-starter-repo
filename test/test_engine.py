from engine.engine_type.capulet_engine import CapuletEngine
from engine.engine_type.sternman_engine import SternmanEngine
from engine.engine_type.willoughby_engine import WilloughbyEngine

import unittest
class TestCalliopeEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 40000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage,last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_False(self):
        current_mileage = 2000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage,last_service_mileage)
        self.assertFalse(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 70000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 50000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        self.assertFalse(engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        light_on = True
        engine = SternmanEngine(light_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        light_on = False
        engine = SternmanEngine(light_on)
        self.assertFalse(engine.needs_service())

