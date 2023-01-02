from typing import List

from source.user.user import User


class Expense:
    """Expenses"""

    def __init__(self,
                 exp_id: str,
                 amount: float,
                 paid_by_user: User,
                 split_among_user: List[User],
                 expense_type: str,
                 name: str = '',
                 description: str = '', **kwargs):
        self._exp_id = exp_id
        self._amount = amount
        self._name = name
        self._description = description
        self._expense_type = expense_type
        self._paid_by_user = paid_by_user
        self._split_among_user = split_among_user
        self._extra = kwargs

    def get_paid_by_user(self):
        return self._paid_by_user

    def get_amount(self):
        return self._amount

    def get_participated_users(self):
        return self._split_among_user

    def get_extra(self):
        return self._extra

    def __repr__(self):
        return f'{self._paid_by_user.get_uuid()} paid {self._amount} for {self._name} and split among ' \
               f'{len( self._split_among_user)} friends by using split type {self._expense_type}'
