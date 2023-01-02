from source.splits.amount_distribution import AmountDistribution
from source.splits.splits import Splits


class PercentageSplits(Splits):
    """Exact Split"""
    @staticmethod
    def convert_percentage_to_actual_value(percentage, total):
        return round(percentage*100/total, 2)

    def validate_and_calculate(self):
        users = self._expense.get_participated_users()
        distribution = self.validate_distribution()
        amount = self._expense.get_amount()
        distribution = [self.convert_percentage_to_actual_value(p, amount) for p in distribution]
        diff = abs(amount - sum(distribution))
        if diff > 0:
            distribution[-1] += diff

        amount_distribution = {u.get_uuid(): AmountDistribution(balance=a, user=u) for u, a in zip(users, distribution)}
        return amount_distribution
