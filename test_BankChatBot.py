import unittest

from BankChatBot import BankAccount

class test_BankChatBot(unittest.TestCase):
    #setup method to create a BankAccount object for each test method
    def setUp(self):
        self.bank = BankAccount()

    #test deposit method in BankAccount class
    #test for correct value
    def test_deposit_returns_correct_value(self):
        final_balance = self.bank.deposit(100)
        self.assertEqual(100, final_balance)

    #test for error if a string is passed
    def test_deposit_returns_type_error_if_a_string(self):
        self.assertRaises(ValueError, self.bank.deposit, "100")

    #test withdraw for correct result
    def test_withdraw_returns_correct_value(self):
        self.bank.deposit(500)
        final_balance = self.bank.withdraw(100)
        self.assertEqual(400, final_balance)

    #test for error if a string is passed
    def test_withdraw_returns_type_error_if_a_string(self):
        self.assertRaises(ValueError, self.bank.withdraw, "100")

    #test for balance check
    def test_balance_check(self):
        self.bank.deposit(100)
        self.bank.withdraw(50)
        self.assertEqual(50, self.bank.balance)

    #test if account exists
    def test_account_exists(self):
        self.assertTrue(self.bank)

    #test if account is an instance of BankAccount
    def test_account_is_instance_of_BankAccount(self):
        self.assertIsInstance(self.bank, BankAccount)

    #test if possible to deposit a negative value
    def test_deposit_negative_value(self):
        self.assertRaises(ValueError, self.bank.deposit, -100)

    #test if possible to withdraw a negative value
    def test_withdraw_negative_value(self):
        self.assertRaises(ValueError, self.bank.withdraw, -100)

    #test if possible to withdraw more than the balance
    def test_withdraw_more_than_balance(self):
        self.assertRaises(ValueError, self.bank.withdraw, 100)

    #test status of account
    def test_account_status(self):
        self.assertEqual("active", self.bank.status)

    #test closing account changes status to closed
    def test_close_account(self):
        self.bank.close_account()
        self.assertEqual("closed", self.bank.status)

    #test if you can deposit after closing account
    def test_deposit_after_closing_account(self):
        self.bank.close_account()
        self.assertRaises(ValueError, self.bank.deposit, 100)

    #test if you can withdraw after closing account
    def test_withdraw_after_closing_account(self):
        self.bank.close_account()
        self.assertRaises(ValueError, self.bank.withdraw, 100)

    #test if account is closed
    def test_account_is_closed(self):
        self.bank.close_account()
        self.assertRaises(ValueError, self.bank.deposit, 100)
        self.assertRaises(ValueError, self.bank.withdraw, 100)

    #test balance must be zero before closing account
    def test_balance_must_be_zero_before_closing_account(self):
        self.bank.deposit(100)
        self.assertRaises(ValueError, self.bank.close_account)

    #test showing current weather from API
    def test_show_current_weather(self):
        self.bank.show_current_weather()
        self.assertTrue(self.bank)

    #test for type error if user input is not an integer
    def test_user_input_is_not_an_integer(self):
        self.assertRaises(TypeError, type(
            self.bank.ask_user_what_they_want_to_do()), str)

    #test for value error if user input is not in range
    def test_user_input_is_not_in_range(self):
        self.assertRaises(ValueError, self.bank.user_choose_task, 6)

    #test to call for withdraw method to empty account before closing account
    def test_withdraw_all_money_before_closing_account(self):
        self.bank.deposit(100)
        self.bank.withdraw_all_money_before_closing_account()
        self.assertEqual(0, self.bank.balance)


if __name__ == '__main__':
    unittest.main()
