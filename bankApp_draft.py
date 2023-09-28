# bank app
import json


class Account:
    def __init__(self, owner, account_id, pin_code, balance,
                 debit):  # debit/Kredit används inte i programmet alls, men ni kan utveckla funktioner så att egenskapen är relevant
        self.owner = owner
        self.account_id = account_id
        self.pin_code = pin_code
        self.balance = balance
        self.debit = debit

    def get_owner(self):  # Igor lade till dessa 3, jag själv vet inte vad de är till men kan ni förklara?
        return self.owner

    def get_account_id(self):
        return self.account_id

    def get_pin_code(self):
        return self.pin_code

    def get_balance(self):
        print(f"{self.owner}, your account balance: {self.balance} SEK")

    def withdraw(self):
        amount = input("Enter the amount to withdraw: ")
        try:
            amount = int(amount)
            if amount < 0:
                print("Cannot withdraw a negative amount.")
            elif amount > self.balance:
                print(f"Cannot withdraw more than your account balance which is: {self.balance} SEK")
            else:
                self.balance -= amount
                print(f"{amount} SEK withdrawn.")
                self.get_balance()
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def deposit(self):
        amount = input("Enter the amount to deposit: ")
        print("Please place the money in the machine.")
        try:
            amount = int(amount)
            if amount < 0:
                print("Cannot deposit a negative amount on .")
            else:
                self.balance += amount
                print(f"{amount} SEK was successfully deposited in your account.")
                self.get_balance()
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def record_debit(self, amount):
        if amount > 0:
            self.debit.append(amount)

    def get_debit(self):
        if self.debit:
            print(f"Debit History for {self.owner}:")
            for i, amount in enumerate(self.debit, start=1):
                print(f"{i}. {amount} SEK")
        else:
            print("No debit history available.")

    def load_accounts():
        try:
            with open("accountlist.json", "r") as file:
                data = json.load(file)

            for account_data in data:
                if "debit" not in account_data:
                    account_data["debit"] = []

            return [Account(account_data["owner"], account_data["account_id"], account_data["pin_code"],
                            account_data["balance"], account_data["debit"]) for account_data in data]
        except FileNotFoundError:
            return []

    def save_accounts(accounts):
        data = [{"owner": account.owner, "account_id": account.account_id, "pin_code": account.pin_code,
                 "balance": account.balance, "debit": account.debit}
                for account in accounts]
        with open("accountlist.json", "w") as file:
            json.dump(data, file, indent=5)

    def login_UI():
        print("*" * 20)
        print("* STOCKHOLM BANK *")
        print("*" * 20)
        accounts = Account.load_accounts()
        user_id = int(input("To log in, enter your id: "))
        pin_code_tries = 3

        for account in accounts:
            if user_id == int(account.account_id):
                while pin_code_tries > 0:
                    user_pincode = input("Enter your pin code: ")
                    for account in accounts:
                        if user_pincode == str(account.pin_code):
                            return account
                    else:  # fel pin code, avslutar programmet nu men kan utvecklas mer så att kontot låses t.ex.
                        pin_code_tries -= 1
                        if pin_code_tries == 0:
                            print("You have entered the wrong pin code too many times. Your account has been locked.")
                            return Account.login_UI()
                        print(f"Pin code incorrect. You have {pin_code_tries} tries left.")
                        continue
        else:
            print("*" * 20)
            print("Account not found.")  # Konto-ID hittades inte
            print("*" * 20)
            print("Try again.")
            return Account.login_UI()  # fortsätt med begäran och ange ID

    def quit(self):  # Funktionen för att avsluta programmet
        print("=================================")
        print("Thank you for using our services!")
        print("=================================")


def main_UI(account):
    if account:
        print(f"Welcome, {account.owner}")
        while True:
            print("*" * 20)
            print("ACTIONS:")
            print("[c]heck balance")
            print("[w]ithdraw")
            print("[d]eposit")
            print("[h]istory")
            print("[q]uit")
            action = input(
                "Select an action: ").lower()  # Metod för att undvika logiska fel vid inmatning av stora bokstäver
            if action == 'c':
                account.get_balance()
            elif action == 'w':
                account.withdraw()
            elif action == 'd':
                account.deposit()
            elif action == 'h':
                account.get_debit()
            elif action == 'q':
                account.quit()  # Anropar funktionen för att avsluta programmet
                break
            else:
                print("Invalid action. Please select a valid option.")


logged_in_account = Account.login_UI()
if logged_in_account:
    main_UI(logged_in_account)
