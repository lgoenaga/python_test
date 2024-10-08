import unittest, os

from faker import Faker

from src.user import User
from src.bank_account import BankAccount

class UserTests(unittest.TestCase):

  def setUp(self) -> None:
    self.faker = Faker(locale='es_CO')
    self.name = self.faker.name()
    self.email = self.faker.email()
    self.user = User(name=self.name, email=self.email)
  
  def test_user_creator(self):
    self.assertEqual(self.user.name, self.name)
    self.assertEqual(self.user.email, self.email)
    
  def test_user_add_account(self):
    bank_account = BankAccount(
      balance=self.faker.random_int(min=100, max=2000, step=50),
      log_file=self.faker.file_name(extension='txt')
    )
    self.user.add_account(account=bank_account)
    self.assertEqual(len(self.user.accounts), 1)
    
  def test_user_various_accounts(self):
      for _ in range(3):
          bank_account = BankAccount(
              balance=self.faker.random_int(min=100, max=2000, step=50),
              log_file=self.faker.file_name(extension='txt')
          )
          self.user.add_account(account=bank_account)

      expected_value = self.user.get_total_balance()
      value = sum(account.get_balance() for account in self.user.accounts)
      self.assertEqual(value, expected_value)

  def tearDown(self) -> None:
      for account in self.user.accounts:
          if os.path.exists(account.log_file):
              os.remove(account.log_file)