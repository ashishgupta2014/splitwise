from source.settings import logger
from source.user.user_expense_balance_sheet import UserExpenseBalanceSheet


class User:
    """App user"""
    def __init__(self, uuid: str, name: str, email: str, mobile: str):
        self._uuid = uuid
        self._name = name
        self._email = email
        self._mobile = mobile
        self._balance = UserExpenseBalanceSheet()

    @staticmethod
    def create(**kwargs):
        """user creation"""
        try:
            uuid = kwargs['uuid']
        except KeyError:
            logger.fatal(f'Without UUID user can not be created')
            return
        name = kwargs.get('name', uuid)
        email = kwargs.get('email', '')
        mobile = kwargs.get('mobile', '')
        return User(uuid=uuid, name=name, email=email, mobile=mobile)

    def get_expense_balance(self):
        return self._balance

    def get_uuid(self):
        return self._uuid

