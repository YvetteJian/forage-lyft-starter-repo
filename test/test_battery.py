from battery.battery_type.nubbin_battery import NubbinBattery
from battery.battery_type.spindler_battery import SpindlerBattery

import unittest
import datetime

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.datetime(2023, 7, 31)
        last_service_date = datetime.datetime(2022, 7, 31)
        battery = NubbinBattery(current_date,last_service_date)
        self.assertFalse(battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime.datetime(2026, 7, 31)
        last_service_date = datetime.datetime(2022, 7, 31)
        battery = NubbinBattery(current_date,last_service_date)
        self.assertTrue(battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.datetime(2023, 7, 31)
        last_service_date = datetime.datetime(2022, 7, 31)
        battery = SpindlerBattery(current_date,last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_False(self):
        current_date = datetime.datetime(2028, 7, 31)
        last_service_date = datetime.datetime(2022, 7, 31)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())