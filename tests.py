import unittest
from unittest.mock import MagicMock
from logic import *


class TestBalanceUpdate(unittest.TestCase):
    def test_balance_update(self):
        existing_number = MagicMock(spec=ClientDevicesORM)
        existing_number.Balance = 100
        duration = 10
        cost = BasicHomeStrategy().calculate_cost(duration)
        new_balance = existing_number.Balance - cost
        expected_new_balance = 100 - (duration * 1.5)
        self.assertEqual(new_balance, expected_new_balance)


if __name__ == '__main__':
    unittest.main()
