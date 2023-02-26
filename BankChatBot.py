import requests


class BankAccount():
    def __init__(self):
        self.balance = 0  # defining the balance variable
        # defining the amount_type variable
        self.amount_type = (int, float, complex)
        self.status = "active"  # defining the status variable
        self.location = "London"  # defining the location variable e.g "London"
        # defining the weather api_key variable
        self.api_key = "435de105baaee5eceab81c4d860d197f"

    def deposit(self, amount):
        #check if account is active
        if self.status == "active":
            if isinstance(amount, self.amount_type):
                #check for negative value
                if amount < 0:
                    raise ValueError("amount must be positive")
                self.balance += amount
                return self.balance
            else:
                raise ValueError("amount must be a number")
        else:
            raise ValueError("account is closed")

    def withdraw(self, amount):
        #check if account is active
        if self.status == "active":
            if isinstance(amount, self.amount_type):
                #check for negative value
                if amount < 0:
                    raise ValueError("amount must be positive")
                #check if amount is greater than balance
                if amount > self.balance:
                    raise ValueError("amount must be less than balance")
                self.balance -= amount
                return self.balance
            else:
                raise ValueError("amount must be a number")
        else:
            raise ValueError("account is closed")

    #close account
    def close_account(self):
        #confirm account is active
        if self.status == "active":
            #confirm balance is zero
            if self.balance != 0:
                raise ValueError("balance must be zero")
            #change status to closed
            self.status = "closed"
            print("Account is now closed")
            self.amount_type = None
        else:
            raise ValueError("account is already closed")

    #show current weather
    def show_current_weather(self):
        #get current weather from API
        url = f'http://api.openweathermap.org/data/2.5/weather?q={self.location}&appid={self.api_key}'
        response = requests.get(url)
        weather = response.json()
        #print current weather
        print(f"Current weather in {self.location} is: " +
              weather["weather"][0]["description"])

    #user to choose task from chatbot based using input from option of above functions
    def user_choose_task(self):
        #get user input
        user_choice = self.ask_user_what_they_want_to_do()
        #check user choice
        #Inquire about the balance
        if user_choice == 1:
            amount = float(self.balance)
            print(f"Your balance is: {amount}")
        # Make a deposit
        elif user_choice == 2:
            amount = float(input("How much would you like to deposit? "))
            self.deposit(amount)
            self.display_post_action_balance()
        # Make a withdrawal
        elif user_choice == 3:
            amount = float(input("How much would you like to withdraw? "))
            self.withdraw(amount)
            self.display_post_action_balance()
        # Close the account
        elif user_choice == 4:
            self.close_account()
        # Show current weather
        elif user_choice == 5:
            self.show_current_weather()
        # Raise error
        else:
            raise ValueError("Please choose a valid option")

    def display_post_action_balance(self):
        print(f"Your new balance is: {self.balance}")

    def ask_user_what_they_want_to_do(self):
        print("1. Inquire about the balance")
        print("2. Make a deposit")
        print("3. Make a withdrawal")
        print("4. Close the account")
        print("5. Show current weather")
        user_input = input("Welcome! What would you like to do from the options: ")
        return int(user_input)

     #withdraw all money before closing account
    def withdraw_all_money(self):
        #check if account is active
        if self.status == "active":
            #check if balance is greater than 0
            if self.balance > 0:
                #withdraw all money
                print(f"Your balance of: {self.balance} must be withdrawn before closing account")
                self.withdraw(self.balance)
            else:
                raise ValueError("balance is already zero")
        else:
            raise ValueError("account is closed")


#function to run the chatbot
def run_chatbot():
    #create instance of BankAccount class
    bank_account = BankAccount()
    #create a loop to keep the chatbot running
    while True:
        #call user_choose_task function
        bank_account.user_choose_task()
        #ask user if they want to continue
        user_input = input("Do you want to continue? (y/n)")
        if user_input == "n":
            print("Goodbye!")
            break


#call run_chatbot function
run_chatbot()