

class UserExpenseBalanceSheet:
    """User expense Balance Sheet"""

    def __init__(self):
        self._transactions = dict()
        self._total_payment = 0
        self._expenses = []

    def get_owe_amount(self):
        owe = 0
        for _, trx in self._transactions.items():
            owe += trx.owe_amount
        return owe

    def get_owe_against_other_user(self):
        return [(uuid, trx.owe_amount) for uuid, trx in self._transactions.items() if trx.owe_amount > 0]

    def get_amount_back_against_other_user(self):
        return [(uuid, trx.get_back_amount) for uuid, trx in self._transactions.items() if trx.get_back_amount > 0]

    def get_back_amount(self):
        amount = 0
        for _, trx in self._transactions.items():
            amount += trx.get_back_amount
        return amount

    def get_transaction(self):
        return self._transactions

    def set_balance_cross_transaction(self, uuid):
        from source.balance_sheet.transaction import Transaction
        self._transactions[uuid] = Transaction(0, 0)

    def set_total_payment(self, amount: float):
        self._total_payment += amount

    def get_total_payment(self):
        return self._total_payment

    def set_expense(self, expense):
        self._expenses.append(expense)

    def get_expense(self):
        return self._expenses
