from source.user.user import User


class Transaction:
    """User Transactions"""
    def __init__(self, owe_amount: float, get_back_amount: float):
        self.owe_amount = owe_amount
        self.get_back_amount = get_back_amount

