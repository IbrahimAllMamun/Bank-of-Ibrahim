import pytest
from project import Bank

def main():
    pass


data = {
        'person_id': 604,
        'full_name': 'Ibrahim All-Mamun',
        'dob': '2000-12-24',
        'email': 'mimamun@isrt.ac.bd',
        'phone_number': '+8801581101890',
        'balance': 690,
        'date_opened': '2024-06-25'
    }

bank = Bank(**data)


def test_balance():
    assert bank.balance == 690

def test_diposit():
    bank.diposit(30)
    assert bank.balance == 720
    bank.diposit(200)
    assert bank.balance == 920


def test_withdraw():
    bank.withdraw(120)
    assert bank.balance == 800
    bank.withdraw(200)
    assert bank.balance == 600


    with pytest.raises(ValueError):
        bank.withdraw(800)



if __name__ == "__main__":
    main()






