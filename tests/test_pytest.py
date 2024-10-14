import pytest
from src.bank_account import BankAccount
  
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"
    a = 3
    b = 4
    assert sum([a, b]) == 7, "Should be 7"
    with pytest.raises(TypeError):
        sum([1, 'two', 3])
    with pytest.raises(AssertionError):
        assert sum([1, 2, 3]) == 7, "Should be 6"
      
    

@pytest.mark.parametrize("amount, expected", [(100, 200), (50, 150), (200, 300)])  
def test_deposit_varius_amounts(amount, expected):
    account  = BankAccount(balance=100, log_file='log.txt')
    new_balance = account.deposit(amount)
    assert new_balance == expected
    