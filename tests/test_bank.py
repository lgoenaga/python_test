import os
import unittest

from src.exceptions import InsufficientFundsError, WithdrawalTimeRestrictionError
from src.bank_account import BankAccount
from unittest.mock import patch

class BankAccountTest(unittest.TestCase):
  
    SERVER = 'A'
  
    def setUp(self) -> None:
        self.account = BankAccount(balance=100, log_file='log.txt')
    
    def tearDown(self) -> None:
      if os.path.exists(self.account.log_file):
        os.remove(self.account.log_file)
        
    def count_lines(self):
        with open(self.account.log_file, 'r') as file:
            return len(file.readlines())
  
    def test_deposit(self):
            self.account.deposit(100)
            self.assertEqual(self.account.balance, 200)

    def test_withdraw(self):
        self.account.withdraw(50)    
        self.assertEqual(self.account.balance, 50)

    def test_balance(self):
        self.assertEqual(self.account.get_balance(), 100)
        
    def test_transaction(self):
        self.account.deposit(200)
        assert os.path.exists('log.txt')
    
    def test_count_transaction(self):
        self.assertEqual(self.count_lines(), 1)
        self.account.deposit(200)
        self.assertEqual(self.count_lines(), 2)
        
    def test_withdraw_raises_error_when_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(2000)
            
    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 8
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 0)
        
    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_hours_Insufficient_Funds(self, mock_datetime):
        mock_datetime.now.return_value.hour = 9
        with self.assertRaises(InsufficientFundsError):
            new_balance = self.account.withdraw(700)
            self.assertEqual(new_balance, 0)
        new_balance = self.account.get_balance()
        self.assertEqual(new_balance, 100)    
        
    @patch("src.bank_account.datetime")
    def test_withdraw_during_Not_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 6
        with self.assertRaises(WithdrawalTimeRestrictionError):
            new_balance = self.account.withdraw(100)
            self.assertEqual(new_balance, 0)
        new_balance = self.account.get_balance()
        self.assertEqual(new_balance, 100)                             
        
    @unittest.skip('Test skipped')
    def test_skip(self):
        self.skipTest('Test skipped')
        self.account.deposit(200)
        self.assertEqual(self.account.balance, 300)
        
    @unittest.skipIf(SERVER == 'A', 'Test skipped')
    def test_skip_if(self):
        self.account.deposit(200)
        self.assertEqual(self.account.balance, 300)
        
    @unittest.skipUnless(SERVER == 'B', 'Test skipped')
    def test_skip_unless(self):
        self.account.deposit(200)
        self.assertEqual(self.account.balance, 300)
        
    @unittest.expectedFailure
    def test_expected_failure(self):
        self.account.deposit(200)
        self.assertEqual(self.account.balance, 50)
        
    def test_deposit_varius_amounts(self):
        amounts = [{'amount': 100, 'expected': 200},
                   {'amount': 50, 'expected': 150},
                   {'amount': 200, 'expected': 300}]
        for amount in amounts:
            with self.subTest(amount=amount):
                self.account = BankAccount(balance=100, log_file='log.txt')
                new_balance = self.account.deposit(amount['amount'])
                self.assertEqual(new_balance, amount['expected'])