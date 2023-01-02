from source.user.user import User


class UserController:
    """User Controller"""

    users = dict()

    @staticmethod
    def show_user_balance(user):
        balance = user.get_expense_balance()
        print('-----------Show Balance---------------')
        print(f'UUID: {user.get_uuid()}')
        print(f'Total Payments: {balance.get_total_payment()}')
        print('Expenses')
        for e in balance.get_expense():
            print(e)
        print()
        print(f'Total Owe Amount: {balance.get_owe_amount()}')
        for u, a in balance.get_owe_against_other_user():
            print(f'You owe {a} amount to {u}')
        print()
        print(f'Get Back Amount: {balance.get_back_amount()}')
        for u, a in balance.get_amount_back_against_other_user():
            print(f'{u} will pay back {a}')

    def create_user(self, uuid):
        self.users[uuid] = User.create(uuid=uuid)

    def get_user(self, uuid):
        return self.users.get(uuid)

    def get_all_user(self):
        return self.users

    def init_user_transactions(self):
        for u_uuid, u in self.users.items():
            u_bal = u.get_expense_balance()
            for o_uuid, _ in self.users.items():
                if u_uuid != o_uuid:
                    u_bal.set_balance_cross_transaction(o_uuid)
