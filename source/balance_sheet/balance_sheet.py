from source.balance_sheet.transaction import Transaction
from source.expense.expense import Expense


class BalanceSheetController:
    """User Balance Sheet"""

    @staticmethod
    def update_user_expense(amount_distribution, expense: Expense):
        paid_by_user = expense.get_paid_by_user()
        amount = expense.get_amount()
        paid_user_balance = paid_by_user.get_expense_balance()
        paid_user_balance.set_total_payment(amount)
        paid_user_balance.set_expense(expense)
        paid_user_transactions = paid_user_balance.get_transaction()
        for uuid, payable in amount_distribution.items():
            if uuid != paid_by_user.get_uuid():
                paid_user_transaction_with_other_user: Transaction = paid_user_transactions.get(uuid)
                other_user_balance = payable.user.get_expense_balance()
                other_user_transactions = other_user_balance.get_transaction()
                other_user_transaction: Transaction = other_user_transactions.get(paid_by_user.get_uuid())

                if other_user_transaction.get_back_amount >= payable.balance:
                    other_user_transaction.get_back_amount -= payable.balance
                    paid_user_transaction_with_other_user.owe_amount -= payable.balance
                elif other_user_transaction.get_back_amount > 0:
                    diff = payable.balance - other_user_transaction.get_back_amount
                    paid_user_transaction_with_other_user.owe_amount -= other_user_transaction.get_back_amount
                    other_user_transaction.get_back_amount = 0
                    other_user_transaction.owe_amount = diff
                    paid_user_transaction_with_other_user.get_back_amount += diff
                else:
                    other_user_transaction.owe_amount += payable.balance
                    paid_user_transaction_with_other_user.get_back_amount += payable.balance


