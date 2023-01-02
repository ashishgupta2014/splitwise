from source.splits.amount_distribution import AmountDistribution
from source.splits.splits import Splits


class ExactSplits(Splits):
    """Exact Split"""

    def validate_and_calculate(self):
        users = self._expense.get_participated_users()
        distribution = self.validate_distribution()
        amount_distribution = {u.get_uuid(): AmountDistribution(balance=a, user=u) for u, a in zip(users, distribution)}
        return amount_distribution
