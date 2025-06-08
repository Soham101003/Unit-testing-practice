import unittest
from bank import BankAccount


class TestBankAccount(unittest.TestCase):

    def test_initial_balance(self):
        acc=BankAccount(100)
        self.assertEqual(acc.balance, 100)
    def test_withdraw(self):
        acc=BankAccount(100)
        acc.withdraw(20)
        self.assertEquals(acc.balance,80)
    def test_deposit(self):
        acc=BankAccount(100)
        acc.deposit(20)
        self.assertEqual(acc.balance, 120)

    def test_withdraw_insufficient(self):
        acc = BankAccount(30)
        with self.assertRaises(ValueError):
            acc.withdraw(50)


if __name__=="__main__":
    unittest.main()