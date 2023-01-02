from source.exceptions.split_exception import SplitwiseValueError
from source.expense.expense import Expense


class Splits:
    """Splits"""
    def __init__(self, expense: Expense):
        self._expense = expense

    def validate_and_calculate(self):
        raise NotImplemented

    def validate_distribution(self):
        extra = self._expense.get_extra()

        if 'distribution' in extra:
            numbers = extra['distribution']
            if not isinstance(numbers, list):
                raise SplitwiseValueError('Amount distribution metric must be a list type')
            elif len(numbers) == 0:
                raise SplitwiseValueError('Amount distribution metric is empty')
        else:
            raise SplitwiseValueError('Amount distribution metric not provided')

        return numbers
