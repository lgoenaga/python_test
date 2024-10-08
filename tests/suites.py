import unittest

from test_bank import BankAccountTest
from test_calculator import TestCalculator

def bank_suite():
    suite = unittest.TestSuite()
    suite.addTest(BankAccountTest('test_deposit'))
    suite.addTest(BankAccountTest('test_withdraw'))
    suite.addTest(BankAccountTest('test_balance'))
    suite.addTest(BankAccountTest('test_transaction'))
    suite.addTest(BankAccountTest('test_count_transaction'))
    return suite

def calculator_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCalculator('test_suma'))
    suite.addTest(TestCalculator('test_resta'))
    suite.addTest(TestCalculator('test_multiplicacion'))
    suite.addTest(TestCalculator('test_division'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(bank_suite())
 #   runner.run(calculator_suite())