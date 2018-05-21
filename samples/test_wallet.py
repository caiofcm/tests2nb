# test_wallet.py

import pytest


def i_am_not_a_test(aow):
    print(aow)
    return 'yes'


def test_default_initial_amount():
    """
    A
    """
    a = 5
    assert(a == 5)


def test_setting_initial_amount():
    """
    Wallet should have a balance of 100
    """
    wallet = Wallet(100)
    assert wallet.balance == 100


def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100

def test_wallet_spend_cash():
    """
    Wallet should have a balance of 100 when initialized 
    with 20 and spent 10
    """
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10


def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)
