# 3:50 ~ 4:08


def account_check(total_length, query_number):
    if query_number < 0 or query_number > total_length:
        return False
    return True


class Bank:
    balance = []

    def __init__(self, balance: List[int]):
        Bank.balance = [0] + balance[:]

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not (
            account_check(len(Bank.balance), account1)
            and account_check(len(Bank.balance), account2)
        ):
            return False

        if Bank.balance[account1] >= money:
            Bank.balance[account1] -= money
            Bank.balance[account2] += money

            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if not account_check(len(Bank.balance), account):
            return False

        Bank.balance[account] += money

        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not account_check(len(Bank.balance), account):
            return False

        if Bank.balance[account] >= money:
            Bank.balance[account] -= money

            return True
        else:
            return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
