from enum import Enum

from source.splits.equal_split import EqualSplitSplits
from source.splits.exact_split import ExactSplits
from source.splits.percentage_split import PercentageSplits


class ExpenseType(Enum):
    EQUAL = 'EQUAL'
    EXACT = 'EXACT'
    PERCENT = 'PERCENT'

    @classmethod
    def expense_factory(cls, expense_type):
        if cls.EXACT.value == expense_type:
            return ExactSplits
        elif cls.EQUAL.value == expense_type:
            return EqualSplitSplits
        elif cls.PERCENT.value == expense_type:
            return PercentageSplits
        raise NotImplemented(f'Currently expense type not supported {expense_type}')
