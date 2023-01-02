from source.splits.amount_distribution import AmountDistribution
from source.splits.splits import Splits


class EqualSplitSplits(Splits):
    """Equal split"""

    def validate_and_calculate(self):
        users = self._expense.get_participated_users()
        amount = self._expense.get_amount()

        equal_payable = round(amount / len(users), 2)
        balance = abs(equal_payable * len(users) - amount)
        amount_distribution = dict()
        if balance > 0:
            amount_distribution[users[-1].get_uuid()] = AmountDistribution(balance=balance,
                                                                           user=users[-1])

        for user in users:
            temp_user = amount_distribution.get(user.get_uuid())
            if temp_user:
                temp_user.balance += equal_payable
            else:
                amount_distribution[user.get_uuid()] = AmountDistribution(balance=equal_payable, user=user)
        return amount_distribution
