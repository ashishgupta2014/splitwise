from source.expense.expense_controller import ExpenseController
from source.settings import logger
from source.user.user_controller import UserController

# https://www.youtube.com/watch?v=I4xf4STXgmU
# https://gitlab.com/shrayansh8/interviewcodingpractise/-/blob/main/src/LowLevelDesign/DesignSplitwise/User/User.java


class Splitwise:
    """Splitwise Application"""
    expense = ExpenseController()
    user_controller = UserController()

    def add_users(self, default_user_count=4):
        """user creation"""
        for i in range(default_user_count):
            uuid = f'u{i+1}'
            self.user_controller.create_user(uuid)
            logger.info(f'user created by uuid {uuid}')
        logger.info(f'{default_user_count} users created')
        self.user_controller.init_user_transactions()

    def demo(self):
        """Just a demo of splitwise"""
        self.add_users()
        paid_by_user = self.user_controller.get_user('u1')
        paid_amount = 1000
        participated_users = [self.user_controller.get_user('u1'),
                              self.user_controller.get_user('u2'),
                              self.user_controller.get_user('u3'),
                              self.user_controller.get_user('u4')]
        split_type = 'EQUAL'
        name = 'Electricity Bill'
        self.expense.create(paid_by_user=paid_by_user,
                            amount=paid_amount,
                            split_among_user=participated_users,
                            expense_type=split_type,
                            name=name)
        print("Electric Bill :")

        for _, user in self.user_controller.get_all_user().items():
            self.user_controller.show_user_balance(user)

        paid_by_user = self.user_controller.get_user('u1')
        paid_amount = 1250
        participated_users = [self.user_controller.get_user('u2'),
                              self.user_controller.get_user('u3')]
        split_type = 'EXACT'
        name = 'Flipkart Shopping'
        self.expense.create(paid_by_user=paid_by_user,
                            amount=paid_amount,
                            split_among_user=participated_users,
                            expense_type=split_type,
                            name=name, distribution=[370, 880])
        print()
        print('Flipkart Shopping')
        for _, user in self.user_controller.get_all_user().items():
            self.user_controller.show_user_balance(user)

        paid_by_user = self.user_controller.get_user('u4')
        paid_amount = 1200
        participated_users = [self.user_controller.get_user('u1'),
                              self.user_controller.get_user('u2'),
                              self.user_controller.get_user('u3'),
                              self.user_controller.get_user('u4')]
        distribution = [40, 20, 20, 20]
        split_type = 'PERCENT'
        name = 'Individual Expense'
        self.expense.create(paid_by_user=paid_by_user,
                            amount=paid_amount,
                            split_among_user=participated_users,
                            expense_type=split_type,
                            name=name, distribution=distribution)
        print()
        print('Individual Expense')
        for _, user in self.user_controller.get_all_user().items():
            self.user_controller.show_user_balance(user)





