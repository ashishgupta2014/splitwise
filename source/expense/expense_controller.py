from typing import List

from source.balance_sheet.balance_sheet import BalanceSheetController
from source.expense.expense import Expense
from source.splits.expense_types import ExpenseType
from source.splits.splits import Splits
from source.user.user import User


class ExpenseController:
    """Expense Controller Business Implementation"""
    _sequence = 0

    def create(self,
               amount: float,
               paid_by_user: User,
               split_among_user: List[User],
               expense_type: str,
               exp_id: str = '',
               name: str = '',
               **kwargs):
        self._sequence += 1
        exp_id = exp_id or f'exp{str(self._sequence)}'
        expense: Expense = Expense(exp_id=exp_id,
                                   amount=amount,
                                   paid_by_user=paid_by_user,
                                   expense_type=expense_type,
                                   split_among_user=split_among_user,
                                   name=name,
                                   **kwargs)
        split_calculator: Splits = ExpenseType.expense_factory(expense_type)(expense=expense)
        amount_distribution = split_calculator.validate_and_calculate()
        BalanceSheetController.update_user_expense(amount_distribution=amount_distribution, expense=expense)
