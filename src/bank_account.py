from datetime import datetime
from src.exceptions import InsufficientFundsError, WithdrawalTimeRestrictionError

class BankAccount:
    def __init__(self, balance, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self.log_transaction('Account created')

    def log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, 'a') as file:
                file.write(f'{message}\n')

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.log_transaction(f'Deposit: {amount}. new balance: {self.balance}')
        return self.balance

    def withdraw(self, amount):
        now = datetime.now()
        if now.hour < 8 or now.hour > 17:
            raise WithdrawalTimeRestrictionError('Withdrawals are only allowed from 8 to 17')     
        if amount > self.balance:
            raise InsufficientFundsError('Insufficient funds')
        if amount > 0:
            self.balance -= amount
            self.log_transaction(f'Withdraw: {amount}. new balance: {self.balance}')
        return self.balance

    def get_balance(self):
        self.log_transaction(f'Balance: {self.balance}')
        return self.balance